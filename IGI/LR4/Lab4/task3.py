import math
import matplotlib.pyplot as plt
import numpy as np
from tabulate import tabulate
from scipy.stats import mode
from safe_input import safe_input

def task3():
    x = safe_input("Enter the value of x (-1 to 1): ", float)
    if not -1 <= x <= 1:
        print("The value of x must be in the range from -1 to 1 inclusive.")
        return

    eps = safe_input("Enter precision eps: ", float)
    if eps <= 0:
        print("Input error. The accuracy must be greater than 0!")
        return

    calculator = SeriesCalculator(x, eps)
    series_value = calculator.calculate_series()
    calculator.calculate_additional_parameters()
    calculator.plot_graphs()

    resultData = [
        [x, calculator.terms_count, series_value, math.asin(x), eps]
    ]
    headers = ["x", "n", "F(X)", "Math F(x)", "eps"]
    print(tabulate(resultData, headers=headers, tablefmt="grid"))

class SeriesCalculator:
    def __init__(self, x, eps):
        self.x = x
        self.eps = eps
        self.series_values = []
        self.terms_count = 0

    def calculate_series(self):
        n = 0
        term = self.x
        sum_series = term

        while abs(term) < self.eps and n < 500:
            self.series_values.append(sum_series)
            n += 1
            term = (math.factorial(2 * n) / (2 ** (2 * n) * (math.factorial(n) ** 2))) * (self.x ** (2 * n + 1) / (2 * n + 1))
            sum_series += term

        self.terms_count = n
        return sum_series

    def calculate_additional_parameters(self):
        if not self.series_values:
            self.mean = self.median = self.mode = self.variance = self.std_dev = None
            print("Не удалось вычислить статистические параметры, так как ряд не сошелся в заданную точность.")
            return

        self.mean = np.mean(self.series_values)
        self.median = np.median(self.series_values)
        mode_result = mode(self.series_values)
        if isinstance(mode_result.mode, np.ndarray):
            self.mode = mode_result.mode[0] if len(mode_result.mode) > 0 else None
        else:
            self.mode = mode_result.mode
        self.variance = np.var(self.series_values)
        self.std_dev = np.std(self.series_values)

    def plot_graphs(self):
        plt.figure(figsize=(10, 6))
        plt.plot(range(1, self.terms_count + 1), self.series_values, label='Series Value', color='blue')
        plt.plot(range(1, self.terms_count + 1), [math.asin(self.x)] * self.terms_count, label='Math F(x)', color='red')
        plt.xlabel('Number of Terms')
        plt.ylabel('Value')
        plt.title('Series Value vs Math F(x)')
        plt.legend()
        plt.text(0.5, 0.5, f'Mean: {self.mean}\nMedian: {self.median}\nMode: {self.mode}\nVariance: {self.variance}\nStd Dev: {self.std_dev}', transform=plt.gca().transAxes)
        plt.savefig('series_graph.png')
        plt.show()