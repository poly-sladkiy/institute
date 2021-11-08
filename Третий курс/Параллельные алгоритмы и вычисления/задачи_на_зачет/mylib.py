from random import random, seed


def create_matrix(n: int = None, sd: int = None) -> list:
    if sd is not None:
        seed(sd)

    if n is None or n <= 0:
        raise ValueError('N is bad arg.')

    else:
        res = []

        for i in range(n):
            res.append([])
            for _ in range(n):
                res[i].append(random())

    return res


def solution(indexes: list, data):
    for sets in indexes:
        for i in sets:
            for j in range(len(data) - 1 - i):
                data[i][j], data[len(data) - j - 1][len(data) - i - 1] = data[len(data) - j - 1][
                                                                             len(data) - i - 1], data[i][j]