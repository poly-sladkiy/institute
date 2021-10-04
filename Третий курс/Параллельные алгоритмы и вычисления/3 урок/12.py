import threading

def worker():
    print('Hello fron Worker')
    threads = []

    for i in range(10):
        t = threading.Thread(target=worker)
        threads.append(t)
        t.start()
