"""
    Newtons method
    dev. by Ignakov Konstantin 19-IVT-3
"""


def func(x: float) -> float:
    return x ** 3 + 0.2 * x ** 2 + 0.5 * x - 1.2


def derivative_1(x: float) -> float:
    return 3 * x ** 2 + 0.4 * x + 0.5


epsilon = 0.001
a = 0
b = 2
xn = 0

if func(a) * derivative_1(a) < 0:
    xn = a
else:
    xn = b

while abs(func(xn)) > epsilon:
    xn = xn - func(xn) / derivative_1(xn)

print(f"Answer: {xn}")
