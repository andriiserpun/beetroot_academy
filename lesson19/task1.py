def with_index(iterable, start=0):
    index = start
    for item in iterable:
        yield index, item
        index += 1
my_list = ['first', 'second', 'third']
for index, value in with_index(my_list, start=1):
    print(index, value)