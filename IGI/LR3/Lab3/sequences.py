import random
from safe_input import safe_input
def get_user_sequence():
    """
    Get a sequence of numbers from the user input until 12 is entered.
    """
    sequence = []
    while True:
        number = safe_input("Enter a number (or 12 to end): ", float)
        if number == 12:
            break
        sequence.append(number)
    return sequence


def generate_random_sequence():
    """
    Generate a sequence of three random numbers and append 12 to the end.
    """
    sequence = [random.uniform(0, 100) for _ in range(3)]
    sequence.append(12)
    return sequence