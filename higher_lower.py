from deck_engine import DeckEngine
from player import Player
from math import ceil
from misc_game_functions import *


class HigherLower(DeckEngine):
    def __init__(self):
        super().__init__()

    # Game Logic
    def game(self):

        # -----SETUP----- #
        # set player 1 name
        player_1 = Player()
        player_1.set_player_name()
        # set 1 or 2 player
        is_two_player = yes_or_no(
            f"Are you playing with another person, {player_1.name}? 'y' or 'n': ")
        # set player 2 name
        player_2 = Player()
        if is_two_player:
            player_2.set_player_name()
        else:
            player_2.name = "CPU"
        # set number of rounds
        total_rounds = int(input("How many rounds would you like to play? "))
        # set hand size
        hand_size = int(input("How many cards in each players hand?"))
        # set ace high or low
        set_ace_low = yes_or_no(
            "Would you like to set Ace as low? 'y' or 'n': ")
        if set_ace_low:
            self.reassign_value("Ace", 1)

        player_1_wins = 0
        player_2_wins = 0
        best_of = ceil(total_rounds / 2)
        while player_1_wins < best_of or player_2_wins < best_of or player_1_wins + player_2_wins == total_rounds:
            # clear the screen and show wins
            clear()
            print(
                f"{player_1.name}'s wins: {player_1_wins}\n{player_2.name}'s wins: {player_2_wins}")
            # hands must reset between rounds
            if len(player_1.hand) > 0 or len(player_2.hand) > 0:
                cards_to_discard = player_1.hand + player_2.hand
                for card in cards_to_discard:
                    self.discard(card)
                player_1.reset_hand()
                player_2.reset_hand()
            # if there's not enough cards remaining in the deck
            # to deal two hands, then the discard pile is added
            # back into the deck
            if len(self.deck) < hand_size * 2:
                self.deck += self.discard_pile
                self.discard_pile = []
            # deal hand according to size
            player_1.hand = self.deal_hand(hand_size)
            player_2.hand = self.deal_hand(hand_size)
            # show each hand
            player_1.show_hand(len(player_1.hand))
            player_2.show_hand(len(player_2.hand))
            # compare total value of hands
            player_1.calculate_score("higher_lower")
            player_2.calculate_score("higher_lower")
            # track rounds won per player
            if player_1.score > player_2.score:
                player_1_wins += 1
            elif player_2.score > player_1.score:
                player_2_wins += 1
            else:
                continue
        # if either player has won more than half the total rounds
        # then they win the game
        if player_1_wins == player_2_wins:
            print("Draw...")
        else:
            if player_1_wins > player_2_wins:
                winner = player_1.name
            elif player_2_wins > player_1_wins:
                winner = player_2.name
            print(f"{winner} wins!")

# test
higher_lower = HigherLower()

higher_lower.game()
