# Connected this one to python virtualenv "mysqlenv"
# which is using python3.6
# Make sure you add your virtualenv to python interpretter

import unittest
import _mysql
from pip._vendor.distlib import database

class ConnectToMySql(unittest.TestCase):

    def setUp(self):
        pass

    def test_connect(self):
        hostname = 'localhost'
        database = 'ztech'
        username = ''
        password = ''

        conn = _mysql.connect(host=hostname, db=database, user=username,
                  passwd=password)
        conn.query('select * from department')
        rs = conn.store_result().fetch_row(how=1, maxrows=0)
        print(rs)
        conn.close()
        self.assertTrue(True)

if __name__=="__main__":
    unittest.main()