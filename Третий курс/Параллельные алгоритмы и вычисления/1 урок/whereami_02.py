import os, sys

print(
    f"My os.getcwd: {os.getcwd()}",
    f"My sys.path: ",
    sep='\n',
    end=''
)

for i in sys.path[:6]:
    print(i)

input("Press enter-key for quit")

