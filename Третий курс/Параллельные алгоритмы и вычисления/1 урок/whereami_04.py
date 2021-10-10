import os, sys
from tkinter import *

lines = '' # ссылка на подготавливаемое текстовое сообщение
lines += ('My os.getcwd : ' + '\n' + os.getcwd() + '\n')

path_lines = sys.path[:6]
lines += ('My sys.path :' + '\n')

for line in path_lines:
    lines +=(line + '\n')

# Строка lines содержит всю необходимую информацию
root = Tk()
text = Text(root, height=10, width=80)

scroll = Scrollbar(root, command=text.yview)

text.configure(yscrollcommand=scroll.set)
text.insert(END, lines)
text.pack(side=LEFT)

scroll.pack(side=RIGHT, fill=Y)
root.mainloop()
