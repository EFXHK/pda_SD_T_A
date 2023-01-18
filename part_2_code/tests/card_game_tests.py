import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):


    def setUp(self):
        self.card = Card("Ace", 1)
        self.card1 = Card("Heart", 2)
        self.card2 = Card("Club", 3)
        self.card3 = Card("Diamond", 4)
        self.card_game = CardGame()
    

    def test_check_for_ace_is_true(self):
        self.card_game.check_for_ace(self.card1)
        self.assertEqual(True, self.card.value == 1)

    def test_check_for_ace_is_false(self):
        self.card_game.check_for_ace(self.card1)
        self.assertEqual(False, self.card.value == 4)

    def test_check_for_highest_card_highest_first(self):
        self.assertEqual (self.card2, self.card_game.highest_card(self.card1, self.card2))

    def test_check_for_highest_card_highest_last(self):
        self.assertEqual (self.card3, self.card_game.highest_card(self.card2, self.card3))

    def test_cards_total(self):
        cards = [
            self.card,
            self.card1,
            self.card2,
            self.card3]
        self.assertEqual("You have a total of 10", self.card_game.cards_total(cards))



#       def check_for_ace(self, card):

#   def highest_card(self, card1, card2):

# def cards_total(self, cards):
#   return "You have a total of" + total 