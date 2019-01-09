#!/usr/bin/python3
"""test for file storage"""
import unittest
import pep8
import json
import os
import MySQLdb
from os import getenv
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.db_storage import DBStorage
from unittest.mock import patch

class TestDBStorage(unittest.TestCase):
    '''this will test the FileStorage'''

    engine = None
    session = None

    @classmethod
    def setUpClass(cls):
        """set up for test"""
        cls.engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                               format(getenv('HBNB_MYSQL_USER'),
                                      getenv('HBNB_MYSQL_PWD'),
                                      getenv('HBNB_MYSQL_HOST'),
                                      getenv('HBNB_MYSQL_DB')),
                               pool_pre_pring=True)
        cls.session = sessionmaker(bind=cls.engine)()

    @classmethod
    def tearDownClass(cls):
        """at the end of the test this will tear it down"""
        cls.session.close()

    def test_pep8_DBStorage(self):
        """Tests pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/engine/db_storage.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_reload(self):
        """ Tests the new all method """
        pass
'''
    def test_new_all_two(self):
        """ Tests the new all method by passing in None """
        storage = FileStorage()
        all_users = storage.all()
        user_count_init = len(all_users.keys())
        user = State()
        all_users = storage.all()
        user_count_after = len(all_users.keys())
        self.assertEqual(user_count_init, user_count_after - 1)

    def test_new_all_three(self):
        """ Tests the new all method by passing in garbage """
        storage = FileStorage()
        all_users = storage.all("dogs")
        user_count_init = len(all_users.keys())
        user = State()
        all_users = storage.all("dogs")
        user_count_after = len(all_users.keys())
        self.assertEqual(user_count_init, user_count_after)

    def test_new(self):
        """test when new is created"""
        storage = FileStorage()
        obj = storage.all()
        user = User()
        user.id = 123455
        user.name = "Kevin"
        storage.new(user)
        key = user.__class__.__name__ + "." + str(user.id)
        self.assertIsNotNone(obj[key])

    def test_reload_filestorage(self):
        """
        tests reload
        """
        self.storage.save()
        Root = os.path.dirname(os.path.abspath("console.py"))
        path = os.path.join(Root, "file.json")
        with open(path, 'r') as f:
            lines = f.readlines()
        try:
            os.remove(path)
        except:
            pass
        self.storage.save()
        with open(path, 'r') as f:
            lines2 = f.readlines()
        self.assertEqual(lines, lines2)
        try:
            os.remove(path)
        except:
            pass
        with open(path, "w") as f:
            f.write("{}")
        with open(path, "r") as r:
            for line in r:
                self.assertEqual(line, "{}")
        self.assertIs(self.storage.reload(), None)

    def test_delete_one(self):
        """ Tests the delete method """
        storage = FileStorage()
        all_users = storage.all(User)
        user_count_init = len(all_users.keys())
        user = User()
        storage.delete(user)
        all_users = storage.all(User)
        user_count_after = len(all_users.keys())
        self.assertEqual(user_count_init, user_count_after)

    def test_delete_two(self):
        """ Tests the delete method by passing in None """
        storage = FileStorage()
        all_users = storage.all(User)
        user_count_init = len(all_users.keys())
        storage.delete()
        all_users = storage.all(User)
        user_count_after = len(all_users.keys())
        self.assertEqual(user_count_init, user_count_after)

    def test_delete_three(self):
        """ Tests the delete method by passing in garbage """
        storage = FileStorage()
        all_users = storage.all(User)
        user_count_init = len(all_users.keys())
        storage.delete("dogs")
        all_users = storage.all(User)
        user_count_after = len(all_users.keys())
        self.assertEqual(user_count_init, user_count_after)
'''
if __name__ == "__main__":
    unittest.main()