import os, sys

print(
    f"My os.getcwd: {os.getcwd()}",
    f"My sys.path:  {sys.path[:6]}",
    sep='\n'
)

input("Press enter-key for quit")
