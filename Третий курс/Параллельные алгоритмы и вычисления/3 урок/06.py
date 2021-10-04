import _thread, time


class AnyClass:
    def __init__(self, x=0):
        self.x = x
    
    def func(self, x):
        print('Start thread number %d' % x)
        self.x += x
    
    def result(self):
        print(self.x)
# END class AnyClass


obj = AnyClass()

for i in range(1, 1001):
    _thread.start_new_thread(obj.func, (i,))

time.sleep(0.000001)
obj.result()

print('Main process exiting.\n')
