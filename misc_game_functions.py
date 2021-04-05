def yes_or_no(prompt):
    """Takes a question to ask as an argument, and prompts the user for input."""
    VALID_INPUTS = ["y", "n"]
    valid_input_received = False
    while not valid_input_received:
        # User will be prompted repeatedly until valid input is given.
        user_input = input(prompt).lower()
        if user_input in VALID_INPUTS:
            valid_input_received = True
        else:
            print("Input not valid.")
    if user_input == "y":
        return True
    return False


def clear():
    for _ in range(20):
        print("\n")


def compare(player_score, cpu_score):
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


def game_end(player, cpu):
    # game_summary is returned as a list from final_check()
    # function in order of use.
    win_text = compare(player.score, cpu.score)
    player.show_hand(len(player.hand))
    print(f"{player.name}'s final score: {player.score}")
    cpu.show_hand(len(cpu.hand))
    print(f"{cpu.name}'s final score: {cpu.score}\n{win_text}")


def inform_user(player, cpu):
    player.show_hand(len(player.hand))
    print(f"{player.name}'s current score: {player.score}")
    cpu.show_hand(1)
    print(f"{cpu.name}'s current score: {cpu.hand[0].value}")
