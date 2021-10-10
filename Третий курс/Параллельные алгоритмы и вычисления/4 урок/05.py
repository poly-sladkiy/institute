import threading
import time

def clock(interval):
    while True:
        print('The time is %s' % time.ctime())
        time.sleep(interval)
# END function clock ------------------------------------------------

t = threading.Thread(target=clock, args=(5,))
t.daemon = True # Запускаемы поток будет демоном
t.start()

print('Main thread exiting.')