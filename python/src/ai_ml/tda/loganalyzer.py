#!/usr/bin/python

# Basic analysis for CPC logs, using python 2.6.6 only
#
# ['[30/Oct/2018:05:00:02', '-0500]', 'HTTP/1.1',
# 'GET', '/cpc-v0/cpc/accounts/489480373/communication-preferences',
# '200', '', '-', '35', 'ms', '-', '-', '-', 'tomcat-http--289', '-', '10.154.6.4']

import getopt
import sys
import csv
import yaml
from datetime import datetime, date, timedelta
import re
import math
from collections import namedtuple
import json
import pprint

class logtimeutil(object):
    @staticmethod
    def get_timestamp(value):
        # round it to minute, drop the seconds
        # This will be used as the group key. No matter where the log is,
        # the timestamp is used in the report

        # ts = ts.replace(second=0, microsecond=0)
        #return ts

        tsformat = '%d/%b/%Y:%H:%M:%S'
        ts = datetime.strptime(value, tsformat)

        # Since datetime is not json serializable, we use string
        return ts.strftime('%Y%m%d-%H%M')

    @staticmethod
    def validate_interval(interval):
        if interval < 1:
            raise ValueError("Time interval must be at least 1 second")
        if 24 * 3600 % interval != 0:
            raise ValueError("Time interval must be a factor of 24 hours")

    @staticmethod
    def generate_time_buckets(mydate, interval):
        logtimeutil.validate_interval(interval)
        count = 24 * 3600 // interval

        if isinstance(mydate, date):
            start = datetime.combine(mydate, datetime.min.time())
        else:
            start = mydate.replace(hour=0, minute=0, second=0, microsecond=0)
        buckets = [start + timedelta(seconds = interval * n) for n in range(count)]
        return buckets

    @staticmethod
    def calculate_bucket(given_time, interval):
        # For example, if interval=60, decide the bucket for 08:49:20
        logtimeutil.validate_interval(interval)
        bucket = (given_time.hour * 3600 + given_time.minute * 60 + given_time.second ) // interval * interval
        hour = bucket // 3600
        minute = (bucket % 3600) // 60
        second = (bucket % 3600) % 60
        return given_time.replace(hour=hour, minute=minute,
            second=second, microsecond=0).strftime('%Y-%m-%dT%H%M%S')

    @staticmethod
    def test_1():
        interval = 600
        buckets = logtimeutil.generate_time_buckets(date(2018, 10, 1), interval)
        print(buckets)
        b = logtimeutil.calculate_bucket(datetime(2018, 10, 1, 8, 15, 32), interval)
        print(b)

class loganalyzer(object):
    def __init__(self, file, generate_data_file=None):
        self.__file = file
        self.__data_file = generate_data_file
        self.__data_fp = None
        self.__data_csv_fp = None
        self.report = {}

    @property
    def interest_pattern(self):
        return self.__ipattern

    @interest_pattern.setter
    def interest_pattern(self, value):
        self.__ipattern = value
        print('PATTERN: ' + self.__ipattern)

    @property
    def interest_fields(self):
        return self.__ifields

    @interest_fields.setter
    def interest_fields(self, value):
        self.__ifields = value
        print('FIELDS: ' + self.__ifields)
        self.Record = namedtuple("Record", self.__ifields)
        if 'timestamp' not in self.Record._fields:
            raise KeyError('Missing "timestamp" in given fields')

    def __report_parameters(self, value):
        self.__parameters = value
    report_parameters = property(None, __report_parameters)

    @property
    def timeformat(self):
        return self.__timeformat

    @timeformat.setter
    def timeformat(self, value):
        self.__timeformat = value

    # add the result to report dictionary, the key is the normally the date
    def add_report(self, rpt_dict):
        rpt_dict.update(self.report)

    # private
    def __process_logfile(self, fplog):
        interval = self.__parameters['interval']
        value = self.__parameters.get('value')
        groups = self.__parameters.get('group_by')

        earliest = None
        latest = None
        for line in fplog:
            m = re.match(self.__ipattern, line)
            if not m:
                continue;

            # make a namedtuple for readability
            rec = self.Record._make(m.groups())
            # print(rec)

            # must have timestamp
            if not rec.timestamp:
                print('Skipped the line without timestamp')
                continue

            if not earliest:
                earliest = rec.timestamp
            latest = rec.timestamp

            if self.__data_csv_fp:
                self.__data_csv_fp.writerow(m.groups())

            # put it into report
            ts = datetime.strptime(rec.timestamp, self.timeformat)
            bucket = logtimeutil.calculate_bucket(ts, interval)
            if bucket not in self.report:
                self.report[bucket] = {}
            bucket_rpt = self.report[bucket]

            # Group by different parameters
            for grpby in groups:
                if grpby.lower() == 'all':
                    hc = 'all'
                elif '+' in grpby: # handle expression
                    hc = '+'.join((rec._asdict().get(g) for g in grpby.split('+')))
                else:
                    hc = rec._asdict().get(grpby)

                if hc not in bucket_rpt:
                    if value:
                        bucket_rpt[hc] = {'count': 0, 'sum': 0, 'max': 0, 'min': 1000000}
                    else:
                        bucket_rpt[hc] = {'count': 0}
                rpt = bucket_rpt[hc]

                rpt['count'] += 1

                if value:
                    # max, min and mean of time
                    # t = int(rec.timeused)
                    t = int(rec._asdict()[value])
                    rpt['sum'] += t
                    if t > rpt['max']:
                        rpt['max'] = t
                    if t < rpt['min']:
                        rpt['min'] = t

        return namedtuple('LogTimeRange', 'timefrom timeto')(earliest, latest)

    def process(self):
        # Check if need to save the data file
        if self.__data_file and self.__ifields:
            self.__data_fp = open(self.__data_file, 'wb')
            self.__data_csv_fp = csv.writer(self.__data_fp)
            self.__data_csv_fp.writerow(self.__ifields.split())

        # Read the file and call process_logfile
        result = tuple()
        if self.__file.endswith('.gz'):
            # TODO: newer python version should use "with"
            import gzip
            try:
                fplog =  gzip.open(self.__file, 'rb')
                result = self.__process_logfile(fplog)
            except Exception as e:
                print(e)
            finally:
                if self.__data_fp:
                    self.__data_fp.close()
                    self.__data_csv_fp.close()
                if fplog:
                    fplog.close()

        else:
            try:
                with open(self.__file, 'rb') as fplog:
                    result = self.__process_logfile(fplog)
            except Exception as e:
                print(e)
            finally:
                if self.__data_fp:
                    self.__data_fp.close()

        # calculate the mean value for each item and for all
        count_all = 0
        sum_all = 0
        for ts, rpt in self.report.items():
            if 'all' in rpt:
                g = rpt['all']
                count_all += g['count']
                if 'sum' in g:
                    g['mean'] = g['sum'] * 1.0 / g['count']
                    sum_all += g['sum']

        print('OVERVIEW REPORT: ', result,
            namedtuple('CPCLogStats', 'sum count mean')(sum_all, count_all,
            sum_all * 1.0 / count_all if count_all != 0 else 0))

def usage():
    print('''
\tUsage: python {0}
\t\t--conf    (-c) conf_file
\t\t--input   (-i) logfile(s)
\t\t--output  (-o) result_file
\t\t--start   (-s) start_datetime --end(-e) end_datetime
\t\t--interval(-v) agg_timespan
\t\t--datafile(-d) intermediate_data_file\n
\texamples:
\t  python loganalyzer.py  -o a1.json -d a2.csv -c cpclogstats.yaml -i performance2018-12-06.16.log -v 600
\t  python loganalyzer.py  -o a3.json -d a4.csv -c cpclogstats.yaml -i service-12-05-2018-1.log -v 600
'''.format(sys.argv[0]))

class logconf(object):
    def __init__(self, filename):
        with open(filename, "r") as fp:
            self.__conf = yaml.load(fp)

    @property
    def conf(self):
        return self.__conf

def build_file_lists(args):
    return [ args['input'] ]

def create_analyzer(args, conf):
    files = build_file_lists(args)

    # Go through configure to check which file to analyze
    if 'reports' not in conf.conf:
        raise KeyError('Must define reports as the top element in configure file')

    for k, v in conf.conf['reports'].items():
        m = re.match(v.get('files'), files[0])
        if not m: continue

        # update configure from command line
        rpt_para = v['report']
        rpt_para['interval'] = int(args.get('interval', 60))

        y = loganalyzer(files[0], args.get('datafile'))
        y.interest_pattern = v['pattern']
        y.interest_fields = v['fields']
        y.report_parameters = v['report']
        y.timeformat = v['timeformat']

        return y
        
if __name__ == '__main__':
    try:
        opts, args = getopt.getopt(sys.argv[1:],
            "i:o:s:e:v:c:d:",
            ["input=", "output=", "start=", "end=", "interval=", "conf=", "datafile="])

        args = {}
        for o, a in opts:
            if o in ("-i", "--input"):
                args['input'] = a
            elif o in ("-o", "--output"):
                args['output'] = a
            elif o in ("-c", "--conf"):
                args['conf'] = a
            elif o in ("-d", "--datafile"):
                args['datafile'] = a
            elif o in ("-s", "--start"):
                args['start'] = a
            elif o in ("-e", "--end"):
                args['end'] = a
            elif o in ("-v", "--interval"):
                args['interval'] = a
            else:
                assert False, usage()
    except getopt.GetoptError as err:
        print '\n\t' + str(err)
        usage()
        sys.exit(2)

    if len(sys.argv) < 2:
        usage()
        sys.exit(1)

    # load configuration file
    if 'conf' not in args:
        args['conf'] = 'loganalyzer.yaml' #default configure file
    conf = logconf(args['conf'])

    # create analyzer and start analyzing
    y = create_analyzer(args, conf)
    if not y:
        usage()
        sys.exit(99)

    y.process()

    reports = {}
    y.add_report(reports)
    if 'output' in args:
        with open(args['output'], 'w') as fp:
            pp = pprint.PrettyPrinter(indent=4, stream=fp)
            pp.pprint(reports)
    else:
        pp = pprint.PrettyPrinter(indent=4)
        pp.pprint(reports)
