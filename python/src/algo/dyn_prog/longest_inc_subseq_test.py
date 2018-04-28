'''
Created on Jul 2, 2017

@author: Lei
'''
import unittest

from dyn_prog import longest_inc_subseq as lis

class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def testVan_der_Corput_sequence(self):
        mylist = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
        lis.trace_lis(mylist)

        mylist = [10, 22, 9, 33, 21, 50, 41, 60, 12, 15, 20, 30, 40, 22, 41]
        lis.trace_lis(mylist)


    def test_lis_fast(self):
        X = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
        print lis.lis_fast(X)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()