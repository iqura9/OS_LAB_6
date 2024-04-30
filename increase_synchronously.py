import threading
from multiprocessing import Value

iterations = 1000
shared_variable = 0
mtx = threading.Lock()

def increase_synchronously(counter, name):
    while True:
        with counter.get_lock():
            local = counter.value
            if local >= iterations:
                break
            counter.value += 1
            print("Потік:", name, "- Значення:", counter.value)

if __name__ == "__main__":
    # Синхронне збільшення
    shared_variable = 0
    counter = Value('i', 0)
    t1 = threading.Thread(target=increase_synchronously, args=(counter,'thread-1',))
    t2 = threading.Thread(target=increase_synchronously, args=(counter,'thread-2',))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
