import _thread

# объект синхронизации, используемый для синхронизации доступа
# из дочерних потоков к разделяемому ресурсу – потоку sys.stdout
mutex = _thread.allocate_lock()

# список объектов синхронизации, используемых главным потоком
# для анализа состояния дочерних потоков
arraymutex = [_thread.allocate_lock() for i in range(5)]

def func1(numb, value):
    # функция, запускаемая в дочернем потоке
    # numb – номер дочернего потока
    # value – количество прогонов цикла внутри потока
    for i in range(value):
        mutex.acquire()
        print('thread[%d] => %d' % (numb, i))
        mutex.release()
    
    # захват объекта блокировки главного потока
    arraymutex[numb].acquire()

def main():
    # цикл запуска дочерних потоков
    for i in range(5):
        _thread.start_new_thread(func1, (i,5))
    
    # цикл перебора элементов списка объектов блокировки
    for mutex in arraymutex:
    
        # пока блокировка не снята - pass...
        # главный поток 'ожидает захвата' всех элементов
        # списка объектов блокировки
        while not mutex.locked(): pass
    
    # главный поток достигает данной точки программы только после
    # того, как будут 'захвачены' все объекты списка arraymutex
    print('Main thread exiting')

if __name__ == '__main__':
    main()
