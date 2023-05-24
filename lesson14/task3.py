# Write a decorator `arg_rules` that validates arguments passed to the function
def arg_rules(max_length, type, contains):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for arg in args:
                if len(arg) > max_length:
                    print(f"argument {arg} have more than {max_length}")
                    return False
                if not isinstance(arg, type):
                    print(f"{arg} argument have a wrong type {type}")
                    return False
                if not all(char in arg for char in contains):
                    print(f"argument {arg} does not contain {contains}")
                    return False
            return func(*args, **kwargs)
        return wrapper
    return decorator
@arg_rules(15, str, ['05', '@'])
def my_function(arg):
    print(f"{arg} drinks pepsi in his brand new BMW!")
    return True

result = my_function("S@SH05")
print(result)