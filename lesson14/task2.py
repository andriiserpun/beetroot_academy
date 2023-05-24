 # Write a decorator that takes a list of stop words and replaces them with * inside the decorated function
 def stop_word_function(func):
    def wrapper(*args, **kwargs):
        print(f"Steve drinks {str(*args)} in his brand new {str(**kwargs)}!")
        return func(*args, **kwargs)
    return wrapper
@stop_word_function(["pepsi", "BMW"])
def create_slogan():
    stop_word_args = [arg if arg not in stop_word_function else "*" for arg in args]
    stop_word_kwargs = [kwarg if kwarg not in stop_word_function else "*" for kwarg in kwargs]
    return f"Steve drinks {stop_word_args} in his brand new {stop_word_kwargs}!"
    print(f"Steve drinks {stop_word_args} in his brand new {stop_word_kwargs}!")
result = create_slogan("Steve drinks pepsi in his brand new BMW!")
print(result)
