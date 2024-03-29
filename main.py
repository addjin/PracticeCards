"""PracticeCards

A project to practice vocabulary.

"""

from card import Card, Deck
import window

card1 = Card("on yuz", "arka yuz")
card2 = Card("表", "裏")

deck = Deck(deckName="Test Deck")

deck.tryadd(card1)
deck.tryadd(card2)

deck["表"]

print(card1)

japDeck = Deck(deckName="Japanese Deck")
japDeck.read("D:\Projects\Scripts_Codes\Jap_vocab\sample", skipsHeader=True)

incompleteDeck = Deck(deckName="Incomplete deck")
incompleteDeck.read("D:\Projects\Scripts_Codes\Jap_vocab\sample2", skipsHeader=True)



window = window.MainWindow()

window.root.mainloop()


print(japDeck)
incompleteDeck