# Note that MySQLdb only supports python2 by now (2/11/2018)
# hence to run this test you need to set interpretter to be python2.7
# by going to "right click -> Run as -> Run Configuration

import unittest
import MySQLdb


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