import _thread, time

def func1(numb, value):
    for i in range(value):
        time.sleep(1)
        mutex.acquire()

        print('thread[%d] => %d' % (numb, i))
        mutex.release()

def main():
    global mutex
    mutex = _thread.allocate_lock()

    for i in range(5):
        _thread.start_new_thread(func1, (i, 5))

    time.sleep(6)
    print('Main process exiting.\n')

if __name__ == '__main__':
    mutex = None
    main()
