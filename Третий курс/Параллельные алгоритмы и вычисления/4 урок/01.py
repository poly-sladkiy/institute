import time

class Profiler(object):
    def __enter__(self):  # Перегруженный метод – вход в объект
        self._startTime=time.time()

    def __exit__(self, type, value, traceback):  # - выход из объекта
        print("Elapsed time: {:.3f} sec".format(
              time.time() - self._startTime))

with Profiler() as p: # Оболочка для исследуемого кода 
    _sum = 0
    for i in range(1, 10000000):
        _sum += i * i
    print("Sum = ", _sum)