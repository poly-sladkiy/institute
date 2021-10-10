import threading

numThread = 1

def fact(n):
    global numThread
    if n < 1:
        print('%s : %d' % ('Thread', numThread))
        numThread += 1
        return 1
    else:
        result = n * fact(n-1)
        print(str(n) + '! = ' + str(result))
        return result
# END function fact -------------------------------------------------

threads = []
for i in range(3,6):
    t = threading.Thread(target=fact, args=(i,))
    threads.append(t)

for thread in threads:
    thread.start()  # Запустить потоки на исполнение

for thread in threads:
    thread.join()   # Ожидать завершения работы дочерних потоков

print('Main thread exiting.')