import sys

sum = 0

while True:
    try:
        line = input()
                              # или sys.input.readlines()
    except EOFError:
                              # или for line in sys.stdin:
         break
                              # input() отсекает символы \n в конце строки
    else:
        sum += int(line)

print(sum)
