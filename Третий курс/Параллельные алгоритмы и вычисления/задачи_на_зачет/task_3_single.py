from time import time
from mylib import create_matrix, solution

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

# Single threads
print("Single thread")
start = time()

solution(indexes, matrix)

print(f'[0][0]: {matrix[0][0]}, [{size - 1}][{size - 1}]: {matrix[size - 1][size - 1]}')
print(f'Time: {time() - start}')
