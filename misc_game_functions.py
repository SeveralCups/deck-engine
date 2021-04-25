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
    """A series of empty print statements to clear the screen."""
    for _ in range(20):
        print("\n")
