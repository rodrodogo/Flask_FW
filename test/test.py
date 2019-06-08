import unittest
from functions import *
import sqlite3


class Test(unittest.TestCase):

    def test_request(self):
        c = dbConector.getInstance()
        _result = c.query("SELECT * FROM person WHERE name = 'rodrigon'")
        self.assertEqual(_result[0]['identification'], 1)

    def test_insert(self):
        c = dbConector.getInstance()
        c.insert("INSERT INTO person VALUES  (5 ,'prueba', 1000)")
        _result = c.query("SELECT * FROM person WHERE identification = 5")
        self.assertEqual(_result[0]['name'], 'prueba')
        c.insert("DELETE FROM person WHERE identification = 5")

if __name__ == '__main__':
    unittest.main()
