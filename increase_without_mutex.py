import threading

iterations = 1000
shared_variable = 0
mtx = threading.Lock()

def increase_without_mutex(name):
    global shared_variable
    for _ in range(iterations):
        shared_variable += 1
        print("Потік:", name, "- Значення:", shared_variable)

if __name__ == "__main__":
    shared_variable = 0
    t1 = threading.Thread(target=increase_without_mutex, args=('thread-1',))
    t2 = threading.Thread(target=increase_without_mutex, args=('thread-2',))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
