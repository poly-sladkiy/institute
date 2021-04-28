import numpy as np

epsilon = 0.001

coefficient = np.array([
    [3.11, -1.66, -0.6, -0.92],
    [-1.65, 3.51, -0.78, 2.57],
    [0.60,  0.78, -1.87, 1.65],
])

def gauss():
    print(f'{"GAUSS":-^40}\n')

    ratios = coefficient.copy()

    for raw in ratios:
        raw /= raw[0]

    for i in range(1, 3):
        ratios[i] -= ratios[0]

    for i in range(1, 3):
        ratios[i] /= ratios[i][1]

    ratios[2] -= ratios[1]
    ratios[2] /= ratios[2][2]

    x3 = ratios[2][3]
    x2 = ratios[1][3] - ratios[1][2] * x3
    x1 = ratios[0][3] - ratios[0][2] * x3 - ratios[0][1] * x2

    print(ratios)
    print(f"x1 = {x1:.4f}\nx2 = {x2:.4f}\nx3 = {x3:.4f}\n")


def iterations():
    print(f'{"ITERATIONS":-^40}\n')

    ratios = coefficient.copy()

    x1_0 = 0
    x2_0 = 0
    x3_0 = 0

    x1 = (ratios[0][3] - (ratios[0][1] * x2_0 + ratios[0][2] * x3_0)) / ratios[0][0]
    x2 = (ratios[1][3] - (ratios[1][0] * x2_0 + ratios[1][2] * x3_0)) / ratios[1][1]
    x3 = (ratios[2][3] - (ratios[2][1] * x2_0 + ratios[2][0] * x3_0)) / ratios[2][2]
    
    while max(abs(x1_0 - x1), abs(x2_0 - x2), abs(x3_0 - x3)) >= epsilon:
        x1_0 = x1
        x2_0 = x2
        x3_0 = x3

        x1 = (ratios[0][3] - (ratios[0][1] * x2_0 + ratios[0][2] * x3_0)) / ratios[0][0]
        x2 = (ratios[1][3] - (ratios[1][0] * x1_0 + ratios[1][2] * x3_0)) / ratios[1][1]
        x3 = (ratios[2][3] - (ratios[2][1] * x2_0 + ratios[2][0] * x1_0)) / ratios[2][2]

    print(f"x1 = {x1:.4f}\nx2 = {x2:.4f}\nx3 = {x3:.4f}\n")


def gaussSeidel():
    print(f'{"GAUSS-SEIDEL":-^40}\n')

    ratios = coefficient.copy()

    x1_0 = 0
    x2_0 = 0
    x3_0 = 0

    x1 = (ratios[0][3] - (ratios[0][1] * x2_0 + ratios[0][2] * x3_0)) / ratios[0][0]
    x2 = (ratios[1][3] - (ratios[1][0] * x2_0 + ratios[1][2] * x3_0)) / ratios[1][1]
    x3 = (ratios[2][3] - (ratios[2][1] * x2_0 + ratios[2][0] * x3_0)) / ratios[2][2]

    while max(abs(x1_0 - x1), abs(x2_0 - x2), abs(x3_0 - x3)) >= epsilon:
        x1_0 = x1
        x2_0 = x2
        x3_0 = x3

        x1 = (ratios[0][3] - (ratios[0][1] * x2_0 + ratios[0][2] * x3_0)) / ratios[0][0]
        x2 = (ratios[1][3] - (ratios[1][0] * x1 + ratios[1][2] * x3_0)) / ratios[1][1]
        x3 = (ratios[2][3] - (ratios[2][1] * x2 + ratios[2][0] * x1)) / ratios[2][2]

    print(f"x1 = {x1:.4f}\nx2 = {x2:.4f}\nx3 = {x3:.4f}\n")


if __name__ == '__main__':
    gauss()
    iterations()
    gaussSeidel()
