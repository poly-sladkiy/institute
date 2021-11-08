from random import seed
from random import random as ran
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


def solution(data, res: list):
    if len(data) == 1:
        res.append(data[0])
    elif len(data) > 1:
        _max = data[0]
        for i in data[1:]:
            if i > _max:
                _max = i
        res.append(_max)


def th_calc(rows, results):
    for row in rows:
        if len(row) < 10:
            solution(row, results)
        else:

            intervals = []
            for i in range(CPU + 1):
                intervals.append(int(len(row) / CPU * i))

            threads = []
            for i in range(CPU):
                tr = Thread(target=solution, args=(row[intervals[i]:intervals[i+1]], results))
                threads.append(tr)

            for thread in threads:
                thread.start()
            for thread in threads:
                thread.join()


def calc(rows, results):
    for row in rows:
        solution(row, results)


CPU = cpu_count()
size = 1000
matrix = create_matrix(size, 42)

data = list(iter_upper_main_diagonal(matrix))
# for i in data:
#     for j in i:
#         print(f'{j:<10.5f}', end='')
#     print()

# Many threads
print("Multithreading")
res = []
start = time()
th_calc(data, res)

answer = []
solution(res, answer)
print(f'Time: {time() - start}')
print(f"Result: {answer[0]}\n")

# One thread
print("Single thread")
res = []
start = time()
calc(data, res)

answer = []
solution(res, answer)
print(f'Time: {time() - start}')
print(f"Result: {answer[0]}")
