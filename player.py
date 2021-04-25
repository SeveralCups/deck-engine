class Player:
    def __init__(self):
        """Players have a name, a hand in the form of a 
        list of card objects, and individual score
        tracking."""
        self.name = "Dealer"
        self.hand = []
        self.score = 0

    def calculate_score(self, game_type):
        # This function is very tailored to blackjack and
        # will need to be reworked.
        new_total = 0
        for card in self.hand:
            new_total += card.value
        if game_type.lower() == "blackjack":
            # Ace can either be 11 or 1;
            # Removes 10 from new total if ace as 11 would
            # result in a losing score.
            has_ace = self.check_for_ace()
            if has_ace and new_total > 21:
                new_total -= 10
            # A Blackjack is a score of 21 with just two cards.
            # Sets score to 0 to differentiate from a score of 21
            # with > 2 cards.
            if len(self.hand) == 2 and new_total == 21:
                new_total = 0
            self.score = new_total
        else:
            self.score = new_total

    def set_player_name(self):
        """Prompts for input and changes the player name."""
        self.name = input("Input your name: ").title()

    def show_hand(self, card_count):
        """Prints the players hand card by card in a human
        readable format."""
        response = f"{self.name}'s hand: "
        for _ in range(card_count):
            response += f"The {self.hand[_].name} of {self.hand[_].suit}. "
        print(response)

    def check_for_ace(self):
        """Checks to see if the player has an ace in their
        hand for score checking."""
        for card in self.hand:
            if card.name == "Ace":
                return True
        return

    def reset_hand(self):
        """Discards all cards in the players hand."""
        self.hand = []
