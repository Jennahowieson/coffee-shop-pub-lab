import unittest
from src.pub import Pub
from src.drink import Drink
from src.customer import Customer

class TestPub(unittest.TestCase):
    def setUp(self):
        drinks = ["vodka", "beer", "wine"]
        self.pub = Pub("White Horse", 200, drinks) 

    def test_pub_has_name (self):
        self.assertEqual("White Horse", self.pub.name)

    def test_pub_has_till (self):
        self.assertEqual (200, self.pub.till)
    
    def test_pub_has_drinks (self):
        self.assertEqual (3,len(self.drinks))