# Connected this one to python virtualenv "mysqlenv"
# which is using python3.6
# Make sure you add your virtualenv to python interpretter

import unittest
import _mysql

class ConnectToMySql(unittest.TestCase):

    def setUp(self):
        pass

    def connect(self):
        hostname = 'localhost'
        username = 'USERNAME'
        password = 'PASSWORD'
        database = 'DBNAME'

        self.assertTrue(True)

if __name__=="__main__":
    unittest.main()