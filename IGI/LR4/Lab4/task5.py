import numpy as np

def task5():
    n = 5
    m = 5

    A = np.random.randint(0, 10, (n, m))

    print("Матрица A:")
    print(A)

    element = A[2, 3]
    print(f"Элемент в позиции (2,3): {element}")

    submatrix = A[1:4, 1:4]
    print("Подматрица:")
    print(submatrix)

    multiplied_matrix = 2 * A
    print("Матрица, умноженная на 2:")
    print(multiplied_matrix)

    mean_value = np.mean(A)
    print(f"Среднее значение: {mean_value}")

    median_value = np.median(A)
    print(f"Медиана: {median_value}")

    corr_coef = np.corrcoef(A)
    print(f"Коэффициент корреляции:")
    print(corr_coef)

    variance = np.var(A)
    print(f"Дисперсия: {variance}")

    std_dev = np.std(A)
    print(f"Стандартное отклонение: {std_dev}")

    min_element = np.min(np.fliplr(A).diagonal())
    print(f"Наименьший элемент на побочной диагонали: {min_element}")

    diag_variance_func = np.var(np.fliplr(A).diagonal())
    print(f"Дисперсия элементов побочной диагонали (через функцию): {diag_variance_func:.2f}")

    diag_variance_formula = np.mean((np.fliplr(A).diagonal() - np.mean(np.fliplr(A).diagonal())) ** 2)
    print(f"Дисперсия элементов побочной диагонали (через формулу): {diag_variance_formula:.2f}")