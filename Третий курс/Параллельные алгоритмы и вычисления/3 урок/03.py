import _thread
from tkinter import *

def child(tid):
    print('Hello from thread %d' % tid)
   
    root = Tk()
    Label(root, text='Hello from thread %d' % tid,
    
    font=('times', 20)).pack()
    root.mainloop()

def parent():
    for i in range(5):
        _thread.start_new_thread(child, (i,))
    
    input('quit - press Enter-key')
    print('Parent thread exiting.')

parent()
