import WarDeck

a_deck = WarDeck.Deck()
a_deck.shuffle()
#print(a_deck)

a_hand = WarDeck.Hand(a_deck)
print(a_hand)