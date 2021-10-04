import _thread, time, math


class Calc:
    def __init__(self, x=0):
        self.x = x #
        self.arr = [] # в список будут заноситься найденные значения
        # по отрезкам интегрирования
    
    def func(self, a, b, step):
        i = a
        res = 0 # 'аккумулятор' для значений функции
        # на отрезке интегрирования
        while i < b:
            res += step * (i * math.sin(i))/2
            i += step
        self.arr.append(res)
    
    def result(self):
        self.x = sum(self.arr) # суммируем найденные значения
        print(self.x)
# END class Calc

obj = Calc(0)
Xa = 4; Xb = 8; step = 0.00001
Xn = Xb - step

numThreads = 100 # количество параллельных потоков
intervX = (Xb - Xa) / numThreads

try:
    xa = Xa
    xb = Xa + intervX
    for i in range(0, numThreads):
        _thread.start_new_thread(obj.func, (xa, xb, step))
        xa += intervX
        xb += intervX
except RuntimeError:
    pass

time.sleep(10)
obj.result()

print('Main process exiting.\n')
