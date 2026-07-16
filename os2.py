from multiprocessing import Process, Queue
import time

def producer(q):
    for i in range(5):
        print("Producer trying to add:", i)
        q.put(i)              
        print("Producer added:", i)

def consumer(q):
    time.sleep(3)            
    for i in range(5):
        item = q.get()        
        print("Consumer removed:", item)
        time.sleep(1)

if __name__ == "__main__":
    q = Queue(maxsize=3)     

    p1 = Process(target=producer, args=(q,))
    p2 = Process(target=consumer, args=(q,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Finished")
