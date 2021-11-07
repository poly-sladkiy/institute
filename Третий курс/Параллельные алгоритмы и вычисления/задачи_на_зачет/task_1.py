from random import seed
from random import random as ran
from multiprocessing import cpu_count
from mylib import ThreadWithReturnValue

CPU = cpu_count()

seed(42)


def create_matrix(n: int = None) -> list:
    if n is None or n <= 0:
        raise ValueError('N is bad arg.')

    else:
        res = []

        for i in range(n):
            res.append([])
            for _ in range(n):
                res[i].append(ran())

    return res


def my_max(arr: list):
    if len(arr) == 1:
        return arr[0]
    else:
        max_elem = arr[0]

        for i in arr[1:]:
            if i > max_elem:
                max_elem = i

        return max_elem


def iter_upper_main_diagonal(mtrx: list):
    if len(mtrx) != len(mtrx[0]):
        raise ValueError('mtrx should be square.')

    iter = 0
    for row in mtrx:
        yield row[iter:]
        iter += 1


matrix = create_matrix(10)

threads = []
results = []

for i in iter_upper_main_diagonal(matrix):
    for tabs, j in enumerate(i):
        print(f'{"   "*tabs}{j:<10.5f}', end='')
    print()
