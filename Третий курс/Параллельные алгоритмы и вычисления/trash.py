from random import random, seed
from multiprocessing import cpu_count
from threading import Thread
from time import time


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


# def swap_items(data):
#     for i in range(len(data) - 1):
#         for j in range(len(data) - 1 - i):
#             data[i][j], data[len(data) - j - 1][len(data) - i - 1] = data[len(data) - j - 1][
#                                                                                  len(data) - i - 1], data[i][j]
#
#
# def swap_items_real():
#     for i in range(len(matrix) - 1):
#         for j in range(len(matrix) - 1 - i):
#             matrix[i][j], matrix[len(matrix) - j - 1][len(matrix) - i - 1] = matrix[len(matrix) - j - 1][
#                                                                                  len(matrix) - i - 1], matrix[i][j]


def solution(indexes: list, data):
    for sets in indexes:
        for i in sets:
            for j in range(len(data) - 1 - i):
                data[i][j], data[len(data) - j - 1][len(data) - i - 1] = data[len(data) - j - 1][
                                                                             len(data) - i - 1], data[i][j]


matrix = create_matrix(1000, 42)
second_matrix = matrix.copy()
size = len(matrix)
print(f'Matrix:\n'
      f'[0][0]: {matrix[0][0]}, [{size - 1}][{size - 1}]: {matrix[size - 1][size - 1]}\n')

# for i in range(size):
#     for j in range(size):
#         print(f'{matrix[i][j]:<10.5f}', end='')
#     print('\n')

indexes = []
for i in range(int(size / 2) + (1 if size % 2 != 0 else 0)):
    a = {i}
    if matrix[size - 1 - i][:i]:
        a.add(size - 1 - i)

    indexes.append(a)

# solution(indexes, matrix)

# Many threads
print("Multithreading")
start = time()

CPU = cpu_count()
intervals = set()
for i in range(CPU + 1):
    intervals.add(len(indexes) // CPU * i)
intervals = sorted(list(intervals))

threads = []
for i in range(CPU - 1):

    tr = Thread(target=solution, args=(indexes[intervals[i]: intervals[i + 1]], matrix))
    threads.append(tr)

for thread in threads:
    thread.start()
for thread in threads:
    thread.join()

print(f'[0][0]: {matrix[0][0]}, [{size - 1}][{size - 1}]: {matrix[size - 1][size - 1]}')
print(f'Time: {time() - start}')

