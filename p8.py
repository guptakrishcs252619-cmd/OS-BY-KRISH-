import threading
import time
import random

mutex = threading.Semaphore(1)
rw_mutex = threading.Semaphore(1)
queue = threading.Semaphore(1)

read_count = 0
shared_data = 0


def reader(reader_id):
    global read_count

    time.sleep(random.uniform(0.1, 1))

    queue.acquire()
    mutex.acquire()

    read_count += 1

    if read_count == 1:
        rw_mutex.acquire()

    mutex.release()
    queue.release()

    print(f"Reader {reader_id} is reading. Shared Data = {shared_data}")
    time.sleep(random.uniform(0.1, 0.5))

    mutex.acquire()

    read_count -= 1

    if read_count == 0:
        rw_mutex.release()

    mutex.release()


def writer(writer_id):
    global shared_data

    time.sleep(random.uniform(0.1, 1))

    queue.acquire()
    rw_mutex.acquire()
    queue.release()

    shared_data += 1

    print(f"Writer {writer_id} is writing. New Shared Data = {shared_data}")
    time.sleep(random.uniform(0.1, 0.5))

    rw_mutex.release()


reader_threads = [
    threading.Thread(target=reader, args=(i,))
    for i in range(3)
]

writer_threads = [
    threading.Thread(target=writer, args=(i,))
    for i in range(2)
]


for thread in reader_threads:
    thread.start()

for thread in writer_threads:
    thread.start()


for thread in reader_threads:
    thread.join()

for thread in writer_threads:
    thread.join()


print("All readers and writers have completed.")
print(f"Final Shared Data = {shared_data}")
print("krish gupta 085")
