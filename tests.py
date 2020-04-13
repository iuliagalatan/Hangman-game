import unittest
from gameserv import *
from domain import *

class Tests(unittest.TestCase):
    def test_add_sentance(self):
        domain = Sentances()
        gameserv = service(domain)
        self.assertRaises(ValueError, gameserv.add_sentance, "a")
        domain = Sentances()
        gameserv = service(domain)
        self.assertRaises(ValueError, gameserv.add_sentance, "an ar")
        domain = Sentances()
        gameserv = service(domain)
        self.assertRaises(ValueError, gameserv.add_sentance, "ana ar")
        domain = Sentances()
        gameserv = service(domain)
        self.assertRaises(ValueError, gameserv.add_sentance, "anna has apples")

    def test_add(self):
        domain = Sentances()

        domain.add('iulia laa plimbare')
        string = domain.sentances[-1]
        self.assertEqual(string, 'iulia laa plimbare')

        domain = Sentances()

        domain.add('zebra coco')
        string = domain.sentances[-1]
        self.assertEqual(string, 'zebra coco')






