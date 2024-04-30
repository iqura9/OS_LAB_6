import threading
import time

lock = threading.Lock()
shared_variable = 0

def thread_function():
    global shared_variable
    for _ in range(10000000):
        lock.acquire()
        shared_variable += 1
        lock.release()

start_time = time.time()

thread1 = threading.Thread(target=thread_function)
thread2 = threading.Thread(target=thread_function)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

end_time = time.time()

print("Час виконання з використанням замка:", end_time - start_time, "секунд")
print("Значення спільної змінної після паралельних обчислень (замок):", shared_variable)
