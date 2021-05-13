# Ньютон
import numpy as np

x = [
    1.340,
    1.345,
    1.350,
    1.355,
    1.360,
    1.365,
    1.370,
    1.375,
    1.380,
    1.385,
    1.390,
    1.395,
]

y = [
    4.25562,
    4.35325,
    4.45522,
    4.56184,
    4.67344,
    4.79038,
    4.91306,
    5.04192,
    5.17744,
    5.32016,
    5.47069,
    5.62968,
]

f = 0
n = 11
f1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
f2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
h = x[1] - x[0]  # шаг

dy = np.eye(n, dtype=float)  # высчитываем дельта
last = n

for i in np.arange(0, n, 1):
    dy[0][i] = y[i]

for i in np.arange(1, n, 1):
    for j in np.arange(0, last - 1, 1):
        dy[i][j] = dy[i - 1][j + 1] - dy[i - 1][j]
    last -= 1


res = dy[1][0]
fact = 1
i = 0
while i < 10:
    q = (x[i] - x[0]) / h
    mult = [0, 1, 2]

    mult[0] = 2 * q - 1
    mult[1] = 3 * q ** 2 - 6 * q + 2
    mult[2] = 4 * q ** 3 - 18 * q ** 2 + 22 * q - 6

    for j in np.arange(2, 4, 1):
        fact *= j
        res += mult[j - 2] / fact * dy[j][0]

    f = (1 / h) * res  # вычисляем первые производные
    f1[i] = f  # запись первых производных
    print(f"f` = {f1[i]:.15f}", sep='')
    i = i + 1  # счетчик
    
print(f'{"":-^20}')

i = 0
res = dy[2][0]
fact = 1
while i < 9:
    q = (x[i] - x[0]) / h
    mult = [0, 1]
    mult[0] = 6 * q - 6
    mult[1] = 12 * q ** 2 - 36 * q + 22
    for j in np.arange(3, 4, 1):
        fact *= j
        res += mult[j - 3] / fact * dy[j][0]
    
    f = (1 / h) * res  # вычисляем первые производные
    f2[i] = f  # запись первых производных
    print(f"f`` = {f2[i]:.15f}", sep='')
    i = i + 1  # счетчик
