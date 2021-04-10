import numpy as np

epsilon = 0.001

coefficient = np.array([
    [3.11, -1.66, -0.6, -0.92],
    [-1.65, 3.51, -0.78, 2.57],
    [0.60,  0.78, -1.87, 1.65],
])


def gauss():
    print(f'{"GAUSS":-^40}')

    ratios = coefficient.copy()

    # Преобразование матрицы

    for row in ratios:
        row /= row[0]
    print(ratios, end='\n\n')

    for i in range(1, ratios.shape()[0]):
        ratios[i] -= ratios[]


if __name__ == '__main__':
    gauss()
