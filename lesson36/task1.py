import asyncio
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
async def compute_tasks(num):
    return (fibonacci(num), factorial(num), square(num), cube(num))
async def main():
    tasks = [compute_tasks(num) for num in range(1, 11)]
    results = await asyncio.gather(*tasks)
    return results
if __name__ == "__main__":
    import time

    start_time = time.time()
    asyncio.run(main())
    print("Time taken using asyncio:", time.time() - start_time, "seconds")