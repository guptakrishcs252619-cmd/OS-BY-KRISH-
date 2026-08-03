# Program 1: Multithreading - Fibonacci Series for Different Numbers
import threading

def fibonacci(n):
    a, b = 0, 1
    print(f"Fibonacci series for {n} terms:")
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print("\n")

numbers = [5, 7, 10]

threads = []

for num in numbers:
    t = threading.Thread(target=fibonacci, args=(num,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("All threads completed.")
print("Krish 085")


# ----------------------------------------------------------
# Program 2: Multithreading - Even, Odd Numbers and Fibonacci
# ----------------------------------------------------------

import threading

def even_odd():
    print("Even Numbers:")
    for i in range(1, 11):
        if i % 2 == 0:
            print(i, end=" ")
    print()

    print("Odd Numbers:")
    for i in range(1, 11):
        if i % 2 != 0:
            print(i, end=" ")
    print()

def fibonacci():
    n = 10
    a, b = 0, 1

    print("Fibonacci Series:")
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()

t1 = threading.Thread(target=even_odd)
t2 = threading.Thread(target=fibonacci)

t1.start()
t2.start()

t1.join()
t2.join()

print("Program Finished.")
print("Krish 085")


# ----------------------------------------------------------
# Program 3: Multiple Threads Generating Fibonacci Series
# ----------------------------------------------------------

import threading

def fibonacci(n):
    a = 0
    b = 1

    print(f"\n{threading.current_thread().name} ({n} terms):")

    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b

    print()

t1 = threading.Thread(target=fibonacci, args=(5,), name="Thread-1")
t2 = threading.Thread(target=fibonacci, args=(8,), name="Thread-2")
t3 = threading.Thread(target=fibonacci, args=(10,), name="Thread-3")

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

print("\nAll Threads Finished.")
print("Krish 085")


# ----------------------------------------------------------
# Program 4: Thread Safety and Synchronization Using Lock
# ----------------------------------------------------------

import threading

shared_count = 0
lock = threading.Lock()

def increment():
    global shared_count

    for i in range(5):
        with lock:
            shared_count += 1
            print(threading.current_thread().name, "->", shared_count)

t1 = threading.Thread(target=increment, name="Thread-1")
t2 = threading.Thread(target=increment, name="Thread-2")
t3 = threading.Thread(target=increment, name="Thread-3")

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

print("\nFinal Value of Shared Variable:", shared_count)
print("Krish 085")
