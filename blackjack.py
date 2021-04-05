from deck_engine import DeckEngine
from player import Player
from misc_game_functions import inform_user, yes_or_no, game_end, clear
from art import logo


# Game logic
def blackjack():
    deck_engine = DeckEngine()
    print(logo)
    player = Player()
    player.set_player_name()
    cpu = Player()
    dealing = True
    while dealing:
        # Deals cards so each hand has 2 cards if empty.
        if len(player.hand) < 2 and len(cpu.hand) < 2:
            player.hand = deck_engine.deal_hand(2)
            cpu.hand = deck_engine.deal_hand(2)

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
                player.hand.append(deck_engine.draw_card())
            else:
                while cpu.score != 0 and cpu.score < 17:
                    cpu.hand.append(deck_engine.draw_card())
                    cpu.calculate_score()
                    dealing = False
    # When the dealing loop is exited the scores are
    # assessed and a winner is declared.
    game_end(player, cpu)
    # User is asked in yes_or_no() if they want
    # to play again.
    play_again = yes_or_no(
        "Do you want to play another game of Blackjack? Type 'y' or 'n': ")
    if not play_again:
        print("Thanks for playing!")
    else:
        clear()
        blackjack()