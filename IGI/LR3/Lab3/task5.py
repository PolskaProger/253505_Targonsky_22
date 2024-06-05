from safe_input import safe_input
def task5():
    # The main program
    # User input for the list
    user_float_list = input_float_list()
    # User input for the parameter C
    c = safe_input("Enter the number C: ",float)
    # Display the results
    print(f"Number of list items larger than C: {count_greater_than_c(user_float_list, c)}")
    print(f"Product of list items located up to the maximum modulo element: {product_before_max(user_float_list)}")
    # Display the list on the screen
    print(f"List of entered numbers: {user_float_list}")

def input_float_list():
    """
    Prompts the user to enter real numbers to create a list.
    Validates the input and returns the list of numbers.
    """
    float_list = []  # Initialize an empty list to store the real numbers
    while True:  # Start an infinite loop for user input
        number = input("Enter a float number (or 'end' to complete the input): ")
        if number == 'end':  # Check if the user wants to end the input
            break
        try:
            float_number = float(number)  # Attempt to convert the input to a real number
            float_list.append(float_number)  # Add the number to the list
        except ValueError:  # Handle the error if the input is not a real number
            print("A non-float number has been entered. Try again.")
    return float_list  # Return the list of real numbers


def count_greater_than_c(float_list, c):
    """
    Counts the number of elements in the list that are greater than the number C.
    """
    return sum(1 for number in float_list if number > c)  # Use a generator expression to count


def product_before_max(float_list):
    """
    Calculates the product of elements in the list located before the maximum absolute value element.
    """
    max_value = max(float_list, key=abs)  # Find the max value by absolute value
    max_index = float_list.index(max_value)  # Get the index of the max value
    if max_index == 0:  # Check if the max value is the first element
        return None
    product = 1  # Initialize the product variable
    for number in float_list[:max_index]:  # Iterate over elements before the max value
        product *= number  # Multiply the elements to get the product
    return product  # Return the product