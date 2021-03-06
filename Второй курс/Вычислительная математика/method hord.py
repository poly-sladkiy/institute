"""
    Hord method
    dev. by Ignakov Konstantin 19-IVT-3
"""


def func(x: float) -> float:
    return x ** 3 + 0.2 * x ** 2 + 0.5 * x - 1.2


def derivative_2(x: float) -> float:
    return 6 * x + 0.4


epsilon = 0.001
a = 0
b = 2
xn = 0

if func(a) * derivative_2(a) < 0:
    xn = a

    while abs(func(xn)) > epsilon:
        xn = xn - func(xn) * (b - xn) / (func(b) - func(xn))

else:
    xn = b

    while abs(func(xn)) > epsilon:
        xn = xn - func(xn) * (xn - a) / (func(xn) - func(a))

print(f"Answer: {xn}")
