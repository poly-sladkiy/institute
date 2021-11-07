import threading
from math import factorial
from multiprocessing import cpu_count


CPU = cpu_count()

res = 0


def function(x: float, n: int) -> float:
    return float(x) ** n / factorial(n)


class Calc:
    def __init__(self, func, x: float, n_start: int, n_end: int):
        if n_end < n_start:
            raise ValueError('End have to be more than start')
        
        self.func = func
        self.x = x
        self.n_start = n_start
        self.n_end = n_end

    def __call__(self):
        global res

        for n in range(self.n_start, self.n_end):
            res += self.func(self.x, n)

    def getRes(self):
        return self._res

def main():
    x = float(input('Enter x> '))
    n = 100

    match input('Command (1 - one thread, 2 - many thread): '):
        case '1':
            Calc(function, x, 0, 100)()

        case '2':
            args = []
            for _ in range(CPU + 1):
                args.append(int((n / CPU) * _))

            threads = []
            for i in range(CPU):
                t = threading.Thread(target=Calc(function, x, args[i], args[i + 1]), args=())
                threads.append(t)

            for thread in threads:
                thread.start()  # Запустить потоки на исполнение

            for thread in threads:
                thread.join()   # Ожидать завершения работы дочерних потоков

        case _:
            print('Bad input.')

    print(f'Result: {res}\n',
          f'Main thread exiting.')


if __name__ == '__main__':
    main()
