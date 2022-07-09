from lazyproperty import lazy_property
import pathlib

class Card:
    
    def __init__(self, front, back):
        self.front = front
        self.back = back

    def __repr__(self) -> str:
        return self.front

class Deck:

    def __init__(self, filename, isFrontCaseSensitive=False, isBackCaseSensitive=False) -> None:
        self._cards = []
        self._isFrontCaseSensitive=isFrontCaseSensitive
        self._isBackCaseSensitive=isBackCaseSensitive

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, cardname):
        
        if not self._isFrontCaseSensitive:
            cardname=cardname.lower()

        return self[cardname]

    def __contains__(self, card) -> bool:
        front = card.front.lower() if card.front else self._isFrontCaseSensitive
        return front in self.CardNames

    @lazy_property
    def CardNames(self) -> list:
        return [repr(card) for card in self._cards]

    def add(card):
        if
    
    def read(path, skipsHeader=False, infoCallback=None):
        skipCount=0
        splitstring=";\t"
        text = pathlib.Path(path).read_text()
        front_back_pairs=text.split(splitstring)

        for fbp in front_back_pairs:
            fbp = fbp.split(splitstring)

