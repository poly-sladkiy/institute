import multiprocessing as ml

def worker():
    print("Worker")


if __name__ == '__main__':
    jobs = []
    for i in range(5):
        p = ml.Process(target=worker)

        jobs.append(p)
        
        p.start()
        p.join()

    input('Finam main process.')
