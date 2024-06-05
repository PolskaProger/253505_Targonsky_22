def task3():
    user_input = input("Enter a string to check: ")  # Prompt the user for a string
    is_binary_number(user_input)  # Call the function with the user input
def binary_check_decorator(func):
    """
    A decorator that logs the result of checking if a string is a binary number.
    """
    def wrapper(text):
        result = func(text)  # Call the function being checked
        if result:
            print(f"The string '{text}' is a binary number.")
        else:
            print(f"The string '{text}' is NOT a binary number.")
        return result
    return wrapper

# Applying the decorator to the is_binary_number function
@binary_check_decorator
def is_binary_number(text):
    """
            Checks if the entered string is a binary number.

            This function takes a string as input and analyzes it to determine
            if it is composed exclusively of the digits 0 and 1, which would
            make it a binary number. It iterates through each character of the
            string and returns False if it finds any character other than '0' or '1'.

            Parameters:
            text (str): The string to be checked.

            Returns:
            bool: True if the string is a binary number, False otherwise.
            """
    # The body of the function remains unchanged
    # Iterate over each character in the string
    for char in text:
        # If the character is not '0' or '1', return False
        if char not in ('0', '1', ' '):
            return False
    # If the loop completes without returning False, it's a binary number
    return True
