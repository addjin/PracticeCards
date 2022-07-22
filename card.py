from lazyproperty import lazy_property
import pathlib

class Card:
    
    def __init__(self, front, back) -> None:
        self.front = front
        self.back = back

    def __repr__(self) -> str:
        return self.front

class Deck:

    def __init__(self, filename = "", isFrontCaseSensitive=False, isBackCaseSensitive=False, isFixedDeck=False, deckName=None) -> None:
        self._cards=[]
        self._isFrontCaseSensitive=isFrontCaseSensitive
        self._isBackCaseSensitive=isBackCaseSensitive
        self.isFixedDeck=isFixedDeck
        self.deckName=deckName

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, card):
        return self._cards[card]

    def __contains__(self, card) -> bool:
        front = card.front if self._isFrontCaseSensitive else card.front.lower()
        return front in self.CardNames

    def __repr__(self) -> str:
        prefix= self.deckName if self.deckName is not None else "New Deck"
        return prefix + "(" + str(len(self)) + " cards)"

    @property
    def CardNames(self) -> list:
        return [repr(card) for card in self._cards]

    def __add(self, card):
        if not card in self:
            self._cards.append(card)
            self._updatesProperties=True
            return True
        else:
            return False

    def tryadd(self, card):
        if self.isFixedDeck:
            return False
            
        return self.__add(self, card)
    
    def read(path, skipsHeader=False, infoCallback=None):
        skipCount=0
        splitstring=";\t"
        text = pathlib.Path(path).read_text()
        front_back_pairs=text.split(splitstring)

        for fbp in front_back_pairs:
            fbp = fbp.split(splitstring)

