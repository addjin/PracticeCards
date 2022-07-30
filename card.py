from lazyproperty import lazy_property
import pathlib
import re

fbpRegex = re.compile(r'(\w+);\t(.+)')

class Card:
    
    def __init__(self, front, back) -> None:
        self.front = front
        self.back = back

    def __repr__(self) -> str:
        return self.front

class Deck:

    def __init__(self, filename = "", isFrontCaseSensitive=False, isBackCaseSensitive=False, isFixedDeck=False, deckName=None) -> None:
        self._cards={}
        self._isFrontCaseSensitive=isFrontCaseSensitive
        self._isBackCaseSensitive=isBackCaseSensitive
        self._isFixedDeck=isFixedDeck
        self._deckName=deckName

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, card):
        return self._cards[card]

    def __contains__(self, card) -> bool:
        front = card.front if self._isFrontCaseSensitive else card.front.lower()
        return front in self.CardNames

    def __repr__(self) -> str:
        prefix= self._deckName if self._deckName is not None else "New Deck"
        length=len(self)
        return prefix + " (" + str(length) + (" cards)" if length != 1 else " card)")

    @property
    def CardNames(self) -> list:
        return [repr(card) for card in self._cards]

    @property
    def IsFixedDeck(self) -> bool:
        return self._isFixedDeck

    def __add(self, card):
        if not card in self:
            self._cards[repr(card)]=card
            return True
        else:
            return False

    def tryadd(self, card):
        if self._isFixedDeck:
            return False
            
        return self.__add(card)
    
    def read(self, path, skipsHeader=False, infoCallback=None):
        skipCount=0
        splitstring=";\t"
        text = pathlib.Path(path).read_text()
        front_back_pairs=text.split("\n")

        if skipsHeader:
            front_back_pairs.pop(0)

        for fbp in front_back_pairs:
            fbpSearch = fbpRegex.search(fbp)
            if fbpSearch is None or len(fbpSearch.groups()) != 2:
                skipCount +=1
                continue
            card = Card(fbpSearch[1], fbpSearch[2])
            if not self.__add(card):
                skipCount +=1

