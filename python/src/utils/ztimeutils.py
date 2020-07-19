# This file is to hold the utilities w.r.t date, time and timezone

# https://en.wikipedia.org/wiki/Coordinated_Universal_Time
# "Coordinated Universal Time (or UTC) is the primary time standard by which the world regulates clocks and time.
# It is within about 1 second of mean solar time at 0° longitude, and is not adjusted for daylight saving time.
# It is effectively a successor to Greenwich Mean Time (GMT)."

# https://en.wikipedia.org/wiki/Unix_time
# Unix time (also known as Epoch time, POSIX time,[1] seconds since the Epoch,[2] or UNIX Epoch time[3]) is a
# system for describing a point in time. It is the number of seconds that have elapsed since the Unix epoch,
# minus leap seconds; the Unix epoch is 00:00:00 UTC on 1 January 1970.
# Leap seconds are ignored,[4] with a leap second having the same Unix time as the second before it,
# and every day is treated as if it contains exactly 86400 seconds.[2]
# Due to this treatment, Unix time is not a true representation of UTC.

# https://codeofmatt.com/please-dont-call-it-epoch-time/
# "Unix timestamps are always based on UTC (otherwise known as GMT).
# It is illogical to think of a Unix timestamp as being in any particular time zone."

import sys
import datetime
import pytz
import argparse
from argparse import RawTextHelpFormatter


class ATimeUtils:
    def __init__(self):
        pass

    @staticmethod
    def unix2dttm(e):
        # From Epoch time to UTC time
        return datetime.datetime.fromtimestamp(e, tz=datetime.timezone.utc)

    @staticmethod
    def timestamp2dttm(millisecond):
        ts = float(millisecond)
        if ts.is_integer():
            # For integer, eg 1524349374099, treat the last 3 digits as milliseconds
            return datetime.datetime.fromtimestamp(millisecond / 1000)
        else:
            # For float, such as 1524349374.099776, treat decimals as milliseconds
            return datetime.datetime.fromtimestamp(millisecond)

    @staticmethod
    def string2dttm(utc_date_str, format):
        return datetime.datetime.strptime(utc_date_str, format)

    @staticmethod
    def print(dttm):
        format = "%Y-%m-%d %H:%M:%S.%f %Z%z"

        t = dttm.astimezone(pytz.utc)
        print("UTCtime:        ", t.strftime(format))

        t = dttm.astimezone(pytz.timezone("US/Eastern"))
        print("US/Eastern time:", t.strftime(format))

        t = dttm.astimezone(pytz.timezone("US/Pacific"))
        print("US/Pacific time:", t.strftime(format))

    @staticmethod
    def test_unix2dttm():
        e = 1524349374
        dttm = ATimeUtils.unix2dttm(e)

        target_1 = datetime.datetime(2018, 4, 21, 22, 22, 54).replace(tzinfo=pytz.utc)
        assert dttm == target_1

        target_2 = target_1.astimezone(pytz.timezone("US/Eastern"))
        assert dttm == target_2

    @staticmethod
    def main():
        ATimeUtils.test_unix2dttm()
        ap = argparse.ArgumentParser(formatter_class=RawTextHelpFormatter,
                                     description="Convert and display date and time" +
                                                 "\nFor example:" +
                                                 "\n    python {} -s '2018-04-01 20:10:56.123+0900' -f '%Y-%m-%d %H:%M:%S.%f%z'".format(sys.argv[0]) +
                                                 "\n    python {} -m 1524349374.344".format(sys.argv[0]) +
                                                 "\n    python {} -u 1524349374".format(sys.argv[0])
                                     )

        ap.add_argument("-u", "--unix", type=int, help="Unix time")
        ap.add_argument("-m", "--milliseconds", type=float, help="Unix time in decimal milliseconds")
        ap.add_argument("-s", "--datetime_string", type=str, help="Date time string")
        ap.add_argument("-f", "--format", type=str, help="Date time string format")

        args = ap.parse_args()

        if args.unix:
            d = ATimeUtils.unix2dttm(args.unix)
            print("Given unix time", args.unix)
        elif args.milliseconds:
            d = ATimeUtils.timestamp2dttm(args.milliseconds)
            print("Given unix time in milliseconds", args.milliseconds)
        elif args.datetime_string:
            if not args.format:
                print("You must provide the format when given a date time string")
                return

            d = ATimeUtils.string2dttm(args.datetime_string, args.format)

        ATimeUtils.print(d)


if __name__ == '__main__':
    ATimeUtils.main()
