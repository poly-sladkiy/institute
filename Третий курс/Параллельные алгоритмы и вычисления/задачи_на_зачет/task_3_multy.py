from mylib import create_matrix, solution
from multiprocessing import cpu_count
from threading import Thread
from time import time

matrix = create_matrix(1000, 56)
second_matrix = matrix.copy()
size = len(matrix)
print(f'Matrix:\n'
      f'[0][0]: {matrix[0][0]}, [{size - 1}][{size - 1}]: {matrix[size - 1][size - 1]}\n')

indexes = []
for i in range(int(size / 2) + (1 if size % 2 != 0 else 0)):
    a = {i}
    if matrix[size - 1 - i][:i]:
        a.add(size - 1 - i)

    indexes.append(a)

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
