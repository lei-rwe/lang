from time import time

def count1():
    st = time()
    [x for x in xrange(10000000) if x%4==0]
    et = time()
    print "xrange takes: ", et - st

def count2():
    st = time()
    [x for x in range(10000000) if x%4==0]
    et = time()
    print "range takes: ", et - st

count1()
count2()
