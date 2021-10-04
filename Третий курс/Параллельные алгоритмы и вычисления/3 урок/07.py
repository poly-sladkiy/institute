import _thread, time


class AnyClass:
    def __init__(self, x=0):
        self.protocol = [] # пустой список
        self.x = x
    
    def func(self, x):
        self.protocol.append(x)
        self.x += x
    
    def result(self):
        print(self.x)
# END class AnyClass


obj = AnyClass()

try:
    for i in range(1, 1001):
     _thread.start_new_thread(obj.func, (i,))
except RuntimeError:
    pass

time.sleep(0.000001)
obj.result()

print('Count %d' % len(obj.protocol))
print('Main process exiting.\n')
