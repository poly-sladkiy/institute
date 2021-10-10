import sys

print('From input stream readed this "%s"' % input())

data = sys.stdin.readline()[:-1]
print('From sys.input readed this "%d"' % int(data))
