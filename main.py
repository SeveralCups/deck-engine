from blackjack import Blackjack

blackjack = Blackjack()
GAMES = {"blackjack": blackjack, "exit": "exit"}


def main():
    """Shows a list of games for the player to choose from
    and runs the corresponding game from the dictionary
    above."""
    print("Games:")
    valid_input = False
    while not valid_input:
        for game in GAMES:
            print("   - " + game)
        user_choice = input("Select a game from the list above: ")
        if user_choice in GAMES:
            if user_choice == "exit":
                return
            else:
                game_to_run = GAMES[user_choice].game
            valid_input = True
    game_to_run()


if __name__ == "__main__":
    main()
