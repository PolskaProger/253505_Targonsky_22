import math
from tabulate import tabulate
from safe_input import safe_input
# This function calculates the value of a function using a power series expansion.
# It takes an argument 'x' and a precision 'eps', and returns the function value
# and the number of terms summed to reach the specified precision.
# The function limits the number of iterations to 500.

def task1():
    def calculate_series(x, eps):
        """
        Calculate the value of the function using power series expansion.

        Parameters:
        x (float): The argument value for which the function is calculated.
        eps (float): The precision of the calculations.

        Returns:
        float: The value of the function.
        int: The number of terms summed in the series.
        """
        n = 0  # Counter for the number of terms summed in the series
        term = x  # The first term of the series
        sum_series = term  # The sum of the series

        # Loop to sum the terms of the series until the specified precision is reached
        # or the maximum number of iterations is exceeded
        while abs(term) < eps and n < 500:
            n += 1  # Increment the term counter
            term = (math.factorial(2 * n) / (2 ** (2 * n) * (math.factorial(n) ** 2))) * (x ** (2 * n + 1) / (2 * n + 1))            # Calculate the next term
            sum_series += term  # Add the term to the sum

        return sum_series, n


    # Example of using the function
    while True:
        x =  safe_input("Enter the value of x (-1 to 1): ",float)  # Prompt the user to enter the value of 'x'
        if -1 <= x <= 1:
            break
        else:
            print("The value of x must be in the range from -1 to 1 inclusive.")
    while True:
        eps = float(input("Enter precision eps: "))  # Prompt the user to enter the precision 'eps'
        if eps <=0:
            print("Input error. The accuracy must be greater than 0!")
        else:
            break
    series_value, terms_count = calculate_series(x, eps)  # Call the function with user inputs

    # Print the results
    resultData=[
        [x,terms_count,series_value,math.asin(x),eps]
    ]
    headers=["x","n","F(X)","Math F(x)","eps"]
    print(tabulate(resultData, headers=headers, tablefmt="grid"))