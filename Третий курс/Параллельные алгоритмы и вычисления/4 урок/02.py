import threading, time
"""
В данном примере из основной программы создаются и запускаются
два дочерних потока. В качестве объекта синхронизации используется глобальная переменная step, значение которой анализируется в цикле основного потока.
"""

def print_time(threadName,delay):
    global step
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print("%s: %s" % (threadName, time.ctime(time.time())))
        step -= 1
# END method print_time

step = 10  # global variable

# BEGIN: Create two threads as follows ------------------------------
try:
    print('Main thread started.')
    threading.Thread(target=print_time, args=('Thread-1', 1)).start()
    threading.Thread(target=print_time, args=('Thread-2', 2)).start()
except:
    print('Error: Unale to start thread.')

while step > 0: pass
print('Main thread finished.')