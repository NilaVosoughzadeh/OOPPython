'''
import unittest
import os
from orm.database import Database
from models.user import User

class TestUserModel(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        Database._db_file = 'test_orm.db'
        Database.connect()
        User.create_table()

    @classmethod
    def tearDownClass(cls):
        Database.close()
        os.remove('test_orm.db')

    def setUp(self):
        Database.execute("DELETE FROM users")

    def test_create_user(self):
        user = User(name="Ali", email="ali@example.com")
        user.save()
        self.assertIsNotNone(user.id)

    def test_get_user(self):
        user = User(name="Sara", email="sara@example.com")
        user.save()
        fetched = User.get(email="sara@example.com")
        self.assertIsNotNone(fetched)
        self.assertEqual(fetched.name, "Sara")

    def test_validation_empty_email(self):
        with self.assertRaises(ValueError):
            user = User(name="Test", email=None)
            user.save()

if __name__ == "main":
    unittest.main()
'''