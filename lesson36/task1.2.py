import multiprocessing
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)
def square(n):
    return n ** 2
def cube(n):
    return n ** 3
def compute_tasks(num):
    return (fibonacci(num), factorial(num), square(num), cube(num))

if __name__ == "__main__":
    import time
    start_time = time.time()
    with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
        results = pool.map(compute_tasks, range(1, 11))

    print("Time taken using multiprocessing:", time.time() - start_time, "seconds")
