import _thread
import time

def child(tid):
    print('Hello from thread %d\n' % tid)
    
def parent():
    for i in range(5):
        # создание и запуск дочернего потока
        _thread.start_new_thread(child, (i+1,))
    #time.sleep(5)
    print('Parent thread finished')

parent()
