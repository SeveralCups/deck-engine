from deck_engine import DeckEngine
from player import Player
from misc_game_functions import inform_user, yes_or_no, clear
from art import logo


class Blackjack(DeckEngine):
    def __init__(self):
        super().__init__()

    def compare(self, player_score, cpu_score):
        # The player would lose if their score went over 21,
        # even if the dealer also went over.
        if not player_score > 21 and not cpu_score > 21 and player_score == cpu_score:
            return "Draw"
        elif player_score == 0:
            return "You got a blackjack; you win!"
        elif cpu_score == 0:
            return "Computer got a blackjack; you lose!"
        elif player_score > 21:
            return "Your score went over 21; you lose!"
        elif cpu_score > 21:
            return "Computer score went over 21; you win!"
        elif player_score > cpu_score:
            return "Your score is higher; you win!"
        else:
            return "Computer score is higher; you lose!"

    def game_end(self, player, cpu):
        """Checks the player against the computer and shows
        the outcome of the game."""
        win_text = self.compare(player.score, cpu.score)
        player.show_hand(len(player.hand))
        print(f"{player.name}'s final score: {player.score}")
        cpu.show_hand(len(cpu.hand))
        print(f"{cpu.name}'s final score: {cpu.score}\n{win_text}")

    # Game logic
    def game(self):
        print(logo)
        player = Player()
        player.set_player_name()
        cpu = Player()
        dealing = True
        while dealing:
            # Deals cards so each hand has 2 cards if empty.
            if len(player.hand) < 2 and len(cpu.hand) < 2:
                player.hand = self.deal_hand(2)
                cpu.hand = self.deal_hand(2)

            # Evaluates score and presents the current state
            # of the game to the player.
            player.calculate_score()
            cpu.calculate_score()
            inform_user(player, cpu)

            # Checks if any win or loss conditions have been met
            # after the initial cards have been dealt.
            if player.score == 0 or cpu.score == 0:
                dealing = False
            elif player.score > 21 or cpu.score > 21:
                dealing = False
            else:
                # User is asked in yes_or_no() if they want
                # another card.
                should_keep_playing = yes_or_no(
                    "Type 'y' to get another card, type 'n' to pass: ")
                if should_keep_playing:
                    player.hand.append(self.draw_card())
                else:
                    while cpu.score != 0 and cpu.score < 17:
                        cpu.hand.append(self.draw_card())
                        cpu.calculate_score()
                        dealing = False
        # When the dealing loop is exited the scores are
        # assessed and a winner is declared.
        self.game_end(player, cpu)
        # User is asked in yes_or_no() if they want
        # to play again.
        play_again = yes_or_no(
            "Do you want to play another game of Blackjack? Type 'y' or 'n': ")
        if play_again:
            clear()
            self.game()
        else:
            print("Thanks for playing!")
