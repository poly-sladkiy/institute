from random import random as ran
from random import seed

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


M = int(input('Enter M: '))
matrix = create_matrix(M)

for i in range(M):
    for j in range(M):
        print(f'{matrix[i][j]:<10.5f}', end='')
    print('\n')
