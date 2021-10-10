import os, sys
from tkinter import Tk, Label, Button, YES, TOP, BOTH

lines = ''
lines += 'My os.getcwd : %s' % os.getcwd() + '\n'

text = sys.path[:6]
lines += 'My sys.path :' + '\n'

for line in text:
    lines += line + '\n'

root = Tk()

lbl = Label(root, text=lines, font=('arial', 12)).pack(
        expand=YES, side=TOP, fill=BOTH)

btn = Button(root, text='Quit', command=root.quit).pack()
root.mainloop()
