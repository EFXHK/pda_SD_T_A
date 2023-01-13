import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):

    def setUp(self):
        self.card1 = Card("Heart", 1)
        self.card2 = Card("Spade", 2)

    
    def test_check_card_shape(self):
        