#!/usr/bin/python

# Basic analysis for CPC logs, using python 2.6.6 only
#
# ['[30/Oct/2018:05:00:02', '-0500]', 'HTTP/1.1',
# 'GET', '/cpc-v0/cpc/accounts/489480373/communication-preferences',
# '200', '', '-', '35', 'ms', '-', '-', '-', 'tomcat-http--289', '-', '10.154.6.4']

import getopt
import os
import sys
from datetime import datetime, date
import csv
from itertools import groupby
import re
import json
import subprocess
import pprint

class cpcloganalyzer:
    LOGSERVERS = ['prdtxlvcpcapp01.clientsys.local','prdtxlvcpcapp02.clientsys.local','prdtxlvcpcapp03.clientsys.local','prdtxlvcpcapp04.clientsys.local']
    LOGDIR = '/app/logdata/logs/cpc'
    LOGACHIVEDIR = '/app/logdata/archive/cpc'

    LocalLogBaseDir = '/app/cpc/logs'
    LocalLogDir = ['cpcprodtx01', 'cpcprodtx02', 'cpcprodtx03', 'cpcprodtx04'] 

    @staticmethod
    def validateLocalDirectories():
        for d in cpcloganalyzer.LocalLogDir:
            folder = '{base}/{dir}'.format(base=cpcloganalyzer.LocalLogBaseDir, dir=d)
            if not os.path.exists(folder):
                os.makedirs(folder)

    @staticmethod
    def create(cpclogfile):
        if cpclogfile == "service.log":
            print(str(datetime.now()) + ' -- Analysis service log file {0}; date {1}; serial {2}'.format(cpclogfile, str(date.today()), 'EMPTY'))
            return service_endpoint(cpclogfile)

        # For daily performance files like performance2018-10-31.16.log
        z = re.match("performance(\d\d\d\d-\d\d-\d\d).(\d\d).log", cpclogfile)
        if z is not None and len(z.groups()) == 2:
            d, t = z.groups()
            print(str(datetime.now()) + ' -- Analysis daily performance log file {0}; date {1}; serial {2}'.format(cpclogfile, d, t))
            return perf_daily(cpclogfile)

        # For service log files like service-10-20-2018-3.log and service.log. Rolling log files
        z = re.match("service-(\d\d-\d\d-\d\d\d\d)-(\d+).log", cpclogfile)
        if z is not None and len(z.groups()) == 2 :
            d, t = z.groups()
            print(str(datetime.now()) + ' -- Analysis service log file {0}; date {1}; serial {2}'.format(cpclogfile, d, t))
            return service_endpoint(cpclogfile)

    @staticmethod
    def build_file_lists(args):
        return [ args['input'] ]

    @staticmethod
    def get_timestamp(value):
        # round it to minute, drop the seconds
        # This will be used as the group key. No matter where the log is,
        # the timestamp is used in the report

        # ts = ts.replace(second=0, microsecond=0)
        #return ts

        tsformat = '%d/%b/%Y:%H:%M:%S'
        ts = datetime.strptime(value[1:], tsformat)

        # Since datetime is not json serializable, we use string
        return ts.strftime('%Y%m%d-%H%M')

    # add the result to report dictionary, the key is the normally the date
    def add_report(self, rpt_dict):
        rpt_dict.update(self.report)

class perf_daily(cpcloganalyzer):
    def __init__(self, cpclogfile):
        self.cpclogfile = cpclogfile
        self.report = {}

    def process_log(self, fplog):
        reader = csv.reader(fplog, delimiter=' ')
        for row in reader:
            # Get the time stamp
            try:
                ts = cpcloganalyzer.get_timestamp(row[0])
            except:
                print('Skipped this record: failed to parse time ', row[0])
                continue

            # put it into report
            if ts not in self.report:
                self.report[ts] = {
                    'count': 0, 'sum': 0, 'max': 0, 'min': 1000000, 'mean': 0,
                    'max_row':'', 'min_row':''}
            rpt = self.report[ts]

            # Group by httpcode
            hc = row[5]
            if hc not in rpt:
                rpt[hc] = 0
            rpt[hc] += 1

            # max, min and mean of time
            t = int(row[8])
            rpt['count'] += 1
            rpt['sum'] += t
            if t > rpt['max']:
                rpt['max'] = t
                rpt['max_row'] = ' '.join(row)
            if t < rpt['min']:
                rpt['min'] = t
                rpt['min_row'] = ' '.join(row)

    def read_log(self):
        # Read the log file into data frame and clean it up
        if self.cpclogfile.endswith('.gz'):
            # TODO: newer python version should use "with"
            import gzip
            try:
                fplog =  gzip.open(self.cpclogfile, 'rb')
                self.process_log(fplog)
            except Exception as e:
                print(e)
            finally:
                if fplog:
                    fplog.close()
        else:
            with open(self.cpclogfile, 'rb') as fplog:
                self.process_log(fplog)

    def read_to_dataframe(self):
        # Read the log file into data frame and clean it up
        self.data = {
            'dttm': [], 'httpm': [], 'acct': [], 'method': [],
            'httpcode': [], 't': [], 'ip': []
        }
        with open(self.cpclogfile, 'rb') as logfile:
            reader = csv.reader(logfile, delimiter=' ')
            for row in reader:
                x, y = row[4].split('/')[4:6]
                self.data['dttm'].append(row[0][1:])
                self.data['httpm'].append(row[3])
                self.data['acct'].append(x)
                self.data['method'].append(y)
                self.data['httpcode'].append(row[5])
                self.data['t'].append(row[8])
                self.data['ip'].append(row[15])

    def analyze(self):
        pp = pprint.PrettyPrinter(indent=4)
        pp.pprint(self.report)
        for ts, rpt in self.report.items():
            try:
                rpt['mean'] = rpt['sum'] * 1.0 / rpt['count']
            except Exception as e:
                pass

class service_endpoint(cpcloganalyzer):
    def __init__(self, cpclogfile):
        self.cpclogfile = cpclogfile
        self.report = {
            'user': {},
            'method': {},
            'endpoint': {},

            'op':{},
            'namespace':{},
            'principal': {},
            'segment': {}
        }

    # 2018-11-01 00:00:12.341 [tomcat-http--117]  INFO endpoint - Request: user=GENAMP method=GET URI=http://prdtxlbcpc00.clientsys.local/cpc-v0/cpc/accounts/885930971/communication-preferences
    def process_end_point_logrow(self, row):
        # Count of user
        user = row[8][5:]
        if not user.isupper():
            if re.match("\w{3}\d{3}", user):
                user = "ASSOC"
            else:
                user = "CLIENT"

        if user not in self.report['user']:
            self.report['user'][user] = 1
        else:
            self.report['user'][user] += 1

        # Count of user
        method = row[9][7:]
        if method not in self.report['method']:
            self.report['method'][method] = 0
        else:
            self.report['method'][method] += 1

        # Count of endpoint
        ep = row[10].split('/')[-1].split()[0]
        if ep not in self.report['endpoint']:
            self.report['endpoint'][ep] = 0
        else:
            self.report['endpoint'][ep] += 1

    # 2018-11-01 12:27:18.692 [tomcat-http--441]  WARN com.tdameri.service.cpc.webserv.CpcRestEndpoint - CPCMON GET-PREF: authID=A000000038992453, level=, namespace=AMER.OAUTHAP, principal=CNSBATCH, segment=AMER, info=
    def process_CPCMON_logrow(self, row):
        op = row[8]
        if op not in self.report['op']:
            self.report['op'][op] = 1
        else:
            self.report['op'][op] += 1

        ns = row[11][10:]
        if ns not in self.report['namespace']:
            self.report['namespace'][ns] = 1
        else:
            self.report['namespace'][ns] += 1

        principal = row[12][10:]
        if not principal.isupper():
            if re.match("\w{3}\d{3}", principal):
                principal = "ASSOC"
            else:
                principal = "CLIENT"

        if principal not in self.report['principal']:
            self.report['principal'][principal] = 1
        else:
            self.report['principal'][principal] += 1

        seg = row[13][8:]
        if seg not in self.report['segment']:
            self.report['segment'][seg] = 1
        else:
            self.report['segment'][seg] += 1


    def read_log(self):
        # Read the log file into data frame and clean it up
        with open(self.cpclogfile, 'rb') as logfile:
            reader = csv.reader(logfile, delimiter=' ')
            for row in reader:
                if 'INFO endpoint - Request' in ' '.join(row):
                    self.process_end_point_logrow(row)
                elif 'CPCMON' in row:
                    self.process_CPCMON_logrow(row)

    def analyze(self):
        pass

def usage():
    print('''
\tUsage: python {0} --input(-i) logfile(s) --output(-o) csvfile --start(-s) start_datetime --end(-e) end_datetime --intv(-v) agg_timespan --target(-p) pattern\n
\texample: python cpclogperf.py -i performance2018-11-30.11.log -o abc.json
'''.format(sys.argv[0]))

def temp():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "i:o:s:e:v", ["input=", "output=", "start=", "end="])
        args = {
            'verbose': False
        }
        for o, a in opts:
            if o == "-v":
                args['verbose'] = True
            elif o in ("-i", "--input"):
                args['input'] = a
            elif o in ("-o", "--output"):
                args['output'] = a
            elif o in ("-s", "--start"):
                args['start'] = a
            elif o in ("-e", "--end"):
                args['end'] = a
            elif o in ("-v", "--intv"):
                args['intv'] = a
            elif o in ("-p", "--pattern"):
                args['pattern'] = a
            else:
                assert False, usage()
    except getopt.GetoptError as err:
        print '\n\t' + str(err)
        usage()
        sys.exit(2)

    if len(sys.argv) < 2:
        usage()
        sys.exit(1)

    reports = {}
    files = cpcloganalyzer.build_file_lists(args)
    y = cpcloganalyzer.create(files[0])
    y.read_log()
    y.analyze()
    y.add_report(reports)
    if 'output' in args:
        with open(args['output'], 'w') as fp:
            fp.write(json.dumps(reports))

def build_file_lists(logfiles, log_file_type, fromtime, totime):
    if log_file_type.lower() == 'perf_daily':
        pattern = 'performance(?P<year>\d{4})-(?P<month>\d{2})-(?P<date>\d{2}).(?P<serial>\d{2}).log'
        shour = True #serial indicates hour
    elif log_file_type.lower() == 'perf':
        pattern = 'performance-(?P<month>\d{2})-(?P<date>\d{2})-(?P<year>\d{4})-(?P<serial>\d+).log'
        shour = False
    elif log_file_type.lower() == 'service':
        pattern = 'service-(?P<month>\d{2})-(?P<date>\d{2})-(?P<year>\d{4})-(?P<serial>\d+).log'
        shour = False
    else:
        raise ValueException('File type can only take "perf_daily", "perf", or "service"')

    files = []

    for filename in logfiles:
        f = filename.split()
        if len(f) == 0: continue
        fn = f[-1]
        m = re.match(pattern, fn)
        if not m: continue

        # first compare date
        x = m.group('year') + m.group('month') + m.group('date') + (m.group('serial') if shour else '')
        if x >= fromtime and x <= totime:
            files.append( [fn, f[4] ] )
    
    return files

if __name__ == '__main__':
    cpcloganalyzer.validateLocalDirectories()

    user = 'zha970'
    # or, with stderr:
    p = subprocess.Popen(["ssh", "zha970@prdtxlvcpcapp01.clientsys.local", "ls -l /app/tomcat/cpc/logs/*"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()
    import pdb; pdb.set_trace()

    filelist = []
    for i, host in enumerate(cpcloganalyzer.LOGSERVERS):
        tocopyfiles = []
        cmd = 'ssh {user}@{hostname} ls -l {logdir} {logarchivedir}'.format(user=user,
               hostname=host, logdir=cpcloganalyzer.LOGDIR, logarchivedir=cpcloganalyzer.LOGACHIVEDIR)
        p = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = p.communicate()
        files = out.split('\n')
        files = build_file_lists(files, "perf_daily", '2018121001', '2018121005')

        for f in files:
            localfile = '{base}/{dir}/{file}'.format(base=cpcloganalyzer.LocalLogBaseDir, dir=cpcloganalyzer.LocalLogDir[i], file=f[0])
            if not os.path.isfile(localfile):
                if f[0].endswith('.gz'):
                    tocopyfiles.append('{dir}/{file}'.format(dir=cpcloganalyzer.LOGACHIVEDIR, file=f[0]))
                else:
                    tocopyfiles.append('{dir}/{file}'.format(dir=cpcloganalyzer.LOGDIR, file=f[0]))

        # Copy the file to local
        cmds = 'scp {user}@{host}:{files} {base}/{dir}'.format(user=user, host=host, files = '\{' + ','.join(tocopyfiles) + '\}',
                base=cpcloganalyzer.LocalLogBaseDir, dir=cpcloganalyzer.LocalLogDir[i])

        p = subprocess.Popen(cmds.split(), stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = p.communicate()

        filelist += files
        break

    print(filelist)

    LocalLogBaseDir = '/app/cpc/logs'
    LocalLogDir = ['cpcprodtx01', 'cpcprodtx02', 'cpcprodtx03', 'cpcprodtx04'] 
