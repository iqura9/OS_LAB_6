import threading

def multiply_element(A, B, result, i, j):
    res = 0
    for k in range(len(A[0])):
        res += A[i][k] * B[k][j]
    result[i][j] = res
    print(f"Обрахунок для [{i},{j}] = {res}")

def multiply_matrices(A, B):
    n = len(A)
    m = len(A[0])
    k = len(B[0])
    result = [[0 for _ in range(k)] for _ in range(n)]

    threads = []
    for i in range(n):
        for j in range(k):
            thread = threading.Thread(target=multiply_element, args=(A, B, result, i, j))
            thread.start()
            threads.append(thread)

    for thread in threads:
        thread.join()

    return result

A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
result = multiply_matrices(A, B)
print("Результат:")
for row in result:
    print(row)
