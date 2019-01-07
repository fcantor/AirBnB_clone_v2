#!/usr/bin/python3
"""test for SQL dev and test setup"""
import unittest
import MySQLdb
from os.path import exists


class TestSQL(unittest.TestCase):
    """This will test our SQL setup"""

    def test_sql_dev_setup(self):
        """Parse through and execute dev sql script"""
        self.assertTrue(exists("setup_mysql_dev.sql"), msg="File Not Found")
        with open("setup_mysql_dev.sql", "r") as f:
            sqlFile = f.readlines()
        sqlFile = [x.strip() for x in sqlFile]
        db = MySQLdb.connect(host="localhost",
                             port=3306,
                             user="root",
                             passwd="root")
        cur = db.cursor()
        for line in sqlFile:
            try:
                cur.execute(line)
                db.commit()
            except MySQLdb.connector.Error as err:
                print("Something went wrong: {}".format(err))
        db.close()

    def test_sql_test_setup(self):
        """Parse through and execute test sql script"""
        self.assertTrue(exists("setup_mysql_test.sql"), msg="File Not Found")
        with open("setup_mysql_test.sql", "r") as f:
            sqlFile = f.readlines()
        sqlFile = [x.strip() for x in sqlFile]
        db = MySQLdb.connect(host="localhost",
                             port=3306,
                             user="root",
                             passwd="root")
        cur = db.cursor()
        for line in sqlFile:
            try:
                cur.execute(line)
                db.commit()
            except MySQLdb.connector.Error as err:
                print("Something went wrong: {}".format(err))
        db.close()

if __name__ == "__main__":
    unittest.main()
