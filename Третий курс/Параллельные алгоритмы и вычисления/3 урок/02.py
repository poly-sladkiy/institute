import threading
import time

def child(tid):
    print('Hello from thread %d' % tid)

def parent():
    for i in range(5):
        # создание дочернего потока
        t = threading.Thread(target=child, args=(i+1,))
        t.start() # запуск дочернего потока

    #time.sleep(5)
    print('Parent thread finished')
    
parent()