#!/usr/bin/python3
"""test for file storage"""
import unittest
import pep8
import json
import os
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.db_storage import DBStorage

@unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db',
                     "Test for Database only")
class TestDBStorage(unittest.TestCase):
    '''this will test the DBStorage'''

    @classmethod
    def setUpClass(cls):
        """set up for test"""
        cls.user = User()
        cls.user.first_name = "Kev"
        cls.user.last_name = "Yo"
        cls.user.email = "1234@yahoo.com"
        cls.storage = FileStorage()

    @classmethod
    def tearDownClass(cls):
        """at the end of the test this will tear it down"""
        del cls.user

    def test_pep8_DBStorage(self):
        """Tests pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/engine/db_storage.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_all(self):
        """tests if all works in File Storage"""
        pass

    def test_new(self):
        """test when new is created"""
        pass

    def test_save(self):
        """ tests save method """
        pass

    def test_reload(self):
        """
        tests reload
        """
        pass

    def test_delete(self):
        """ Tests the delete method """
        pass

if __name__ == "__main__":
    unittest.main()
