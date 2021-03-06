"""
    Bisection method
    dev. by Ignakov Konstantin 19-IVT-3
"""


def func(x: float) -> float:
    return x ** 3 + 0.2 * x ** 2 + 0.5 * x - 1.2


epsilon = 0.001
a = 0
b = 2

while abs(a - b) > epsilon:
    cur_a = func(a)
    cur_b = func(b)

    cur_xi = func((a + b) / 2)

    if cur_a * cur_xi > 0:
        a = (a + b) / 2
    else:
        b = (a + b) / 2

print(f'Ответ {(a + b) / 2}')
