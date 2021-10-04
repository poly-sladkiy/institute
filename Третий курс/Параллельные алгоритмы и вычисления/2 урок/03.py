import _thread

def child(tid):
    print('>> Hello from thread %d ' % tid)

def parent():
    i = 0
    while True:
        i += 1
        _thread.start_new_thread(child, (i, ))
        if input(">> Parent thread <quit?> ") == 'q':
            break
    print(">> Buy-buy")

parent()
