import pygame as pygame

class Card:

    def __init__(self, suit, number):
        self._suit=suit
        self._number=number

    def __repr__(self):
        return self._number + " of " + self._suit
    
    @property
    def suit(self):
        return self._suit

    @suit.setter
    def suit(self, suit):
        if suit in ["hearts", "clubs", "diamonds", "spades"]:
            self._suit = suit
        else:
            print("That's not a suit")
            
    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, number):
        if number in CardNumbers:
            self._number=number
        else:
            print("That's not in the deck")