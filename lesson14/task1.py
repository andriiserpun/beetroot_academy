# Write a decorator that prints a function with arguments passed to it.
# NOTE! It should print the function, not the result of its execution!
def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Function to {func.__name__} with {args}")
        return func(*args, **kwargs)
    return wrapper
@logger
def add(x, y):
    return x + y
@logger
def square_all(*args):
    return [arg ** 2 for arg in args]
add(4, 5)
square_all(4, 5)