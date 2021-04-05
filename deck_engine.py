from card import Card
from random import choice

NAMES = {"Ace": 11, "Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6,
         "Seven": 7, "Eight": 8, "Nine": 9, "Ten": 10, "Jack": 10, "Queen": 10, "King": 10}
SUITS = ["Spades", "Clubs", "Hearts", "Diamonds"]


class DeckEngine:
    def __init__(self):
        self.deck = []
        self.discard_pile = []
        self.build_deck()

    def build_deck(self):
        for suit in SUITS:
            for name in NAMES:
                new_card = Card(name, suit, NAMES[name])
                self.deck.append(new_card)
        # print(self.deck)
        self.card_count()

    def card_count(self):
        """Prints how many cards are currently in the deck. 
        Intended for debugging."""
        print(f"There are {len(self.deck)} cards in the deck.")

    def deal_hand(self, hand_size):
        print(f"Dealing hand of size {hand_size}.")
        cards = []
        for _ in range(hand_size):
            new_card = self.draw_card()
            cards.append(new_card)
        self.card_count()
        return cards

    def draw_card(self):
        print("Drawing a card.")
        new_card = choice(self.deck)
        self.deck.remove(new_card)
        return new_card

    def discard(self, card):
        self.discard_pile.append(card)