import os

my_pid = os.getpid()
parent_pid = os.getppid()

print("Hello from priocess number %d" % my_pid)
print(parent_pid)
