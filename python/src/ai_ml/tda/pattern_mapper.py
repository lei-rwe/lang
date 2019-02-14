#!/usr/bin/python

# Following the MapReduce idea, this program is used to extract log data into a file
# which can be used later for analysis

# This program takes a filename and a pattern to extract interested fields

import getopt
import sys
import re

class pattern_mapper(object):
    def __init__(self, file, pattern, fields):
        self.__file = file
        self.__pattern = pattern
        self.__fields = fields

    @property
    def interest_pattern(self):
        return self.__pattern

    @interest_pattern.setter
    def interest_pattern(self, value):
        self.__pattern = value
        print('PATTERN: ' + self.__pattern)

    @property
    def interest_fields(self):
        return self.__fields

    @interest_fields.setter
    def interest_fields(self, value):
        self.__fields = value
        print('FIELDS: ' + self.__fields)

    # private
    def __process_logfile(self, fplog):
        for line in fplog:
            m = re.match(self.__pattern, line)
            if not m:
                continue;
            print(','.join(m.groups()))


    def process(self):
        if self.__file.endswith('.gz'):
            # TODO: newer python version should use "with"
            import gzip
            try:
                fplog =  gzip.open(self.__file, 'rb')
                self.__process_logfile(fplog)
            except Exception as e:
                print(e)
            finally:
                if fplog:
                    fplog.close()

        else:
            try:
                with open(self.__file, 'rb') as fplog:
                    result = self.__process_logfile(fplog)
            except Exception as e:
                print(e)

def usage():
    print('''
\tUsage: python {0}
\t\t--input   (-i) logfile(s)
\t\t--pattern (-p) pattern\n
\t\t--pattern (-f) fields\n
\texamples:
\t  python pattern_mapper.py  -p '\[(\S*) \S*\] [^ ]* (\S*) \S*/(\S*) (\d*)[^\d]*(\d*) ms.*- ([\d\.]*)' -f 'timestamp method url httpcode timeused ip' -i performance2018-12-14.03.log
'''.format(sys.argv[0]))

if __name__ == '__main__':
    try:
        opts, args = getopt.getopt(sys.argv[1:],
            "i:p:f:",
            ["input=", "pattern=", "fields="])

        args = {}
        for o, a in opts:
            if o in ("-i", "--input"):
                args['input'] = a
            elif o in ("-p", "--pattern"):
                args['pattern'] = a
            elif o in ("-f", "--fields"):
                args['fields'] = a
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
    y = pattern_mapper(file=args['input'], pattern=args['pattern'], fields=args['fields'])
    if not y:
        usage()
        sys.exit(99)

    print(','.join(args['fields'].split()))
    y.process()
