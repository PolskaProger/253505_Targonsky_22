from safe_input import safe_input
from sequences import get_user_sequence, generate_random_sequence


def task2():
    def sum_cubes(numbers):
        """
        Sum the cubes of numbers in the provided sequence.

        Parameters:
        numbers (list): The sequence of numbers to sum the cubes of.

        Returns:
        int: The total sum of the cubes of the numbers.
        """
        return sum(number ** 3 for number in numbers)

    # Ask the user to choose the method of sequence initialization
    method = safe_input("Enter '1' to input your own sequence, or '2' to generate a random sequence: ", int)

    if method == 1:
        numbers = get_user_sequence()
    elif method == 2:
        numbers = generate_random_sequence()
        print(f"Generated random numbers: {numbers[:-1]}")
    else:
        print("Invalid input. Exiting the program.")
        return

    # Calculate and print the sum of cubes
    print(f"Sum of cubes of numbers: {int(sum_cubes(numbers))}")
