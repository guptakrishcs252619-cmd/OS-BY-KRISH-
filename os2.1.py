from multiprocessing import Process, Queue

def producer(q):
    for i in range(5):
        print("Produced:", i)
        q.put(i)

def consumer(q):
    for i in range(5):
        item = q.get()
        print("Consumed:", item)

if __name__ == "__main__":
    q = Queue()

    p1 = Process(target=producer, args=(q,))
    p2 = Process(target=consumer, args=(q,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Finished")
