from multiprocessing import cpu_count
import threading
import math

CPU = cpu_count()

res = 0

def function(x: float, n: int) -> float:
    return float(x) ** n / math.fact(n)


class Calc:
    def __init__(self, func, x: float, n_start: int, n_end: int):
        if n_end < n_start:
            raise Exeption('End have to be more than start')
        
        self.func = func
        self.x = x
        self.n = n
        self.n_start = n_start
        self.n_end = n_end

    def __call__(self):
        global res

        for n in range(self.n_start, self.n_end):
            res += self.func(x, n)

    def getRes(self):
        return self._res


x = input('Enter x> ')
n = 100

c = Calc(function, x, 0, 100)

# args = []
# for _ in range(CPU + 1):
#     args.append(int((n / CPU) * _))

# threads = []
# for i in range(CPU):
#     t = threading.Thread(target=Calc(function, x, args[i], args[i + 1]), args=())
#     threads.append(t)

# for thread in threads:
#     thread.start()  # Запустить потоки на исполнение

# for thread in threads:
#     thread.join()   # Ожидать завершения работы дочерних потоков


print(f'Result: {res}\n',
      f'Main thread exiting.')