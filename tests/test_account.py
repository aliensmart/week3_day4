import os
from unittest import TestCase

from app import ORM, Account
from data import schema, seed

DIR = os.path.dirname(__file__)
DBFILENAME = "_test.db"
DBPATH = os.path.join(DIR, DBFILENAME)

ORM.dbpath = DBPATH

class TestAccount(TestCase):

    def setUp(self):
        schema(DBPATH)
        seed(DBPATH)

    def tearDown(self):
        os.remove(DBPATH)
        
    def test_login(self):
        mike_bloom = Account.login("mike_bloom", 'password')
        self.assertIsNotNone(mike_bloom, "account and password find data")
        self.assertIsInstance(mike_bloom, Account, "login returns Account object")
        self.assertEqual(mike_bloom.balance, 10000.00)

    def testOnePosition(self):
        account = Account(username = "Abdoul", password_hash ="abdoulname", balance = 20000)
        self.assertEqual(account.username, "Abdoul")
        self.assertEqual(account.password_hash, "abdoulname")
        self.assertEqual(account.balance, 20000)
        self.assertIsInstance(account,Account)
    
    def testSave(self):
        account = Account(username = "Abdoul", password_hash ="abdoulname", balance = 20000)
        account.save()
        self.assertEqual(account.pk, 2)
        self.assertEqual(account.username, "Abdoul")
        self.assertEqual(account.password_hash, "abdoulname")
        self.assertEqual(account.balance, 20000)
        self.assertIsInstance(account,Account)

        account = Account(pk = 2, username = "Abdoul", password_hash ="abdoulname", balance = 25000)
        account.save()
        self.assertEqual(account.pk, 2)
        self.assertEqual(account.username, "Abdoul")
        self.assertEqual(account.password_hash, "abdoulname")
        self.assertEqual(account.balance, 25000)
        self.assertIsInstance(account,Account)

    def testDelete(self):
        account = Account(pk=2)
        account.delete()
        self.assertEqual(account.username, None)

        
