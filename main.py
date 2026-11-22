import random

RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
SUITS = ["Hearts", "Diamonds", "Clubs", "Spades"]

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        
class Deck:
    def __init__(self):
        self.cards = []
        for rank in RANKS:
            for suit in SUITS:
                self.cards.append(Card(rank, suit))

    def shuffle(self):
        random.shuffle(self.cards)

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

def main():
    deck = Deck()
    deck.shuffle()
    
if __name__ == "__main__":
    main()