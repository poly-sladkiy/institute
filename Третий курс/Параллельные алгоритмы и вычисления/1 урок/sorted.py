import sys

lines = sys.stdin.readlines() # читает строки данных из sys.stdin
lines.sort() # сортировка строк встроенным методом

for line in lines: # цикл перебора считанных и отсортированных строк
    print(line, end='') # вывод строк в стандартный поток вывода
