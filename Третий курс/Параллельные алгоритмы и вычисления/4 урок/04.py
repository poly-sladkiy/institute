import threading
import time


class Clock(threading.Thread):
    def __init__(self, interval):
        threading.Thread.__init__(self)
        self.daemon = True
        self.interval = interval
    # END method __init__() -----------------------------------------

    def run(self):
        while True:
            print('Текущее время: %s' % time.ctime())
            time.sleep(self.interval)
    # END method run ------------------------------------------------
# END class Clock ---------------------------------------------------


t = Clock(3)
t.start()

t.join()  # Процесс можно сделать неуправляемым...
print('Main thread exiting.')