from card import Card
from random import choice

NAMES = {"Ace": 11, "Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6,
         "Seven": 7, "Eight": 8, "Nine": 9, "Ten": 10, "Jack": 10, "Queen": 10, "King": 10}
SUITS = ["Spades", "Clubs", "Hearts", "Diamonds"]


class DeckEngine:
    def __init__(self):
        """Builds a deck of card objects, and prepares a 
        discard pile as an empty list."""
        self.deck = []
        self.discard_pile = []
        self.build_deck()

    def build_deck(self):
        """Populates the deck list with card objects."""
        print("Building new deck...")  # Debug line
        for suit in SUITS:
            for name in NAMES:
                new_card = Card(name, suit, NAMES[name])
                self.deck.append(new_card)
        # print(self.deck)
        self.card_count()  # Debug line

    def card_count(self):
        """Prints how many cards are currently in the deck. 
        Intended for debugging."""
        print(f"There are {len(self.deck)} cards in the deck.")

    def deal_hand(self, hand_size):
        print(f"Dealing hand of size {hand_size}.")  # Debug line
        cards = []
        for _ in range(hand_size):
            new_card = self.draw_card()
            cards.append(new_card)
        self.card_count()
        return cards

    def draw_card(self):
        """Returns a random card from the deck and removes it
        from the self.deck list."""
        print("Drawing a card.")  # Debug line
        new_card = choice(self.deck)
        self.deck.remove(new_card)
        return new_card

    def discard(self, card):
        """Adds a card to the discard pile."""
        self.discard_pile.append(card)

    def reassign_value(self, card_name, new_value):
        """Allows for the value of all of any type of card in 
        the deck to accomodate multiple rulesets."""
        print(
            f"Reassigning the value of all {card_name}'s in the deck to {new_value}.")  # Debug line
        for card in self.deck:
            if card.name == card_name.title():
                card.value = new_value

# ---------- TEST CODE ----------

# deck_engine = DeckEngine()

# for card in deck_engine.deck:
#     if card.name == "Ace":
#         print(card.name + ": " + str(card.value))

# deck_engine.reassign_value("Ace", 4)

# for card in deck_engine.deck:
#     if card.name == "Ace":
#         print(card.name + ": " + str(card.value))
