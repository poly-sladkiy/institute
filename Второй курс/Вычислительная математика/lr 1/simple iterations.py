import random

def func(x: int):
	return x * x * x + 0.2 * x * x + 0.5 * x - 1.2


def gfunc(x: int):
	return (-0.2 * x * x - 0.5 * x + 1.2) ** (1. / 3.)


a = 0
b = 1
epsilon = 0.001

prevx = random.random() * (b - a) + a
curx = gfunc(prevx)

while abs(curx - prevx) > epsilon:
	prevx = curx
	curx = gfunc(prevx)

print(f"Answer: {curx}")