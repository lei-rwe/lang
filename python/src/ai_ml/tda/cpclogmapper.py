#!/usr/bin/python

# Following the MapReduce idea, this program is used to extract log data into a file
# which can be used later for analysis

# This program takes a filename and a pattern to extract interested fields

import getopt
import sys
import datetime
import glob

from pattern_mapper import pattern_mapper

class cpclogmapper(object):
    LOGDIR = '/app/logdata/logs/cpc'
    LOGACHIVEDIR = '/app/logdata/archive/cpc'

    LGT_PERF = 'perf'
    LGT_PERF_DAILY = 'daily_perf'
    LGT_SERV = 'service'

    def __init__(self, ptype, pdate):
        self.__type = ptype

        if not isinstance(pdate, datetime.date):
            self.__date = datetime.datetime.strptime(pdate, '%Y%m%d').date()
        else:
            self.__date = pdate

        if self.__type.lower() == cpclogmapper.LGT_PERF_DAILY:
            self.__pattern = '\[(\S*) \S*\] [^ ]* (\S*) \S*/(\S*) (\d*)[^\d]*(\d*) ms.*- [\d\.]*'
            self.__fields = 'timestamp method url httpcode timeused'
        else:
            raise ValueError('Unsupported value for log type')

    # Based on the given date, get all the candiate log files
    def build_logfile_list(self):
        files = []
        if self.__type.lower() == cpclogmapper.LGT_PERF_DAILY:
            f1 = 'performance{0}.*.log'.format( self.__date.strftime('%Y-%m-%d') )
            files += [x for x in glob.glob("{dir}/{fpattern}".format(dir=cpclogmapper.LOGDIR, fpattern=f1))]

            f2 = 'performance{0}.*.log*.gz'.format( self.__date.strftime('%Y-%m-%d') )
            files += [x for x in glob.glob("{dir}/{fpattern}".format(dir=cpclogmapper.LOGACHIVEDIR , fpattern=f2))]

        files.sort()
        return files

    def process(self):
        files = self.build_logfile_list()

        for f in files:
            y = pattern_mapper(file=f, pattern=self.__pattern, fields=self.__fields)
            if y:
                y.process()

def usage():
    print('''
\tUsage: python {0}
\t\t--type (-t) log_type [{1}|{2}|{3}]
\t\t--date (-d) date(yyyymmdd)
\t\t--save (-s)

\texamples:
\t  python cpclogmapper.py  -t daily_perf -d 20181210
'''.format(sys.argv[0], cpclogmapper.LGT_PERF, cpclogmapper.LGT_PERF_DAILY, cpclogmapper.LGT_SERV))

if __name__ == '__main__':
    try:
        opts, args = getopt.getopt(sys.argv[1:],
            "t:d:s",
            ["type=", "date=", "save"])

        args = {}
        for o, a in opts:
            if o in ("-t", "--type"):
                args['type'] = a
            elif o in ("-d", "--date"):
                args['date'] = a
            elif o in ("-s", "--save"):
                args['save'] = True
            else:
                assert False, usage()

    except getopt.GetoptError as err:
        print '\n\t' + str(err)
        usage()
        sys.exit(2)

    if len(sys.argv) < 2:
        usage()
        sys.exit(1)

    # create mapper
    y = cpclogmapper(ptype=args['type'], pdate=args['date'])
    if not y:
        usage()
        sys.exit(99)

    y.process()
