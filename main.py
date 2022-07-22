"""PracticeCards

A project to practice vocabulary.

"""

from card import Card, Deck

card1 = Card("Front", "Back")
card2 = Card("Fr", "Ba")

deck = Deck()

deck.tryadd(card1)

deck["Front"]

print(card1)