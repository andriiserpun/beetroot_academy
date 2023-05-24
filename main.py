def arg_rules(max_length, type_, contains):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for arg in args:
                if not isinstance(arg, type_):
                    print(f"Аргумент {arg} не является типом {type_}.")
                    return False
                if len(arg) > max_length:
                    print(f"Аргумент {arg} превышает максимальную длину {max_length}.")
                    return False
                if not all(char in arg for char in contains):
                    print(f"Аргумент {arg} не содержит все символы из списка {contains}.")
                    return False
            return func(*args, **kwargs)
        return wrapper
    return decorator
@arg_rules(15, str, ['a', 'b', 'c'])
def my_function(arg):
    print(f"Вызвана функция с аргументом {arg}.")
    return True

result = my_function("abchdsgfhjs")
print(result)
