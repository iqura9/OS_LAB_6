import threading
import numpy as np
import time

def multiply_element(A, B, result, i, j):
    res = 0
    for k in range(len(A[0])):
        res += A[i][k] * B[k][j]
    result[i][j] = res

def multiply_matrices(A, B, num_threads):
    n = len(A)
    m = len(A[0])
    k = len(B[0])
    result = np.zeros((n, k))

    def worker(start, end):
        for i in range(start, end):
            for j in range(k):
                multiply_element(A, B, result, i, j)

    threads = []
    chunk_size = n // num_threads
    for i in range(num_threads):
        start = i * chunk_size
        end = start + chunk_size if i < num_threads - 1 else n
        thread = threading.Thread(target=worker, args=(start, end))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    return result

A = np.random.rand(20, 20)
B = np.random.rand(20, 20)

num_threads_list = [1, 2, 4, 8] 
for num_threads in num_threads_list:
    start_time = time.time()
    multiply_matrices(A, B, num_threads)
    end_time = time.time()
    print(f"Час виконання з {num_threads} потоками: {end_time - start_time} секунд")
