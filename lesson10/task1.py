def oops():
    try:
        names = {'one': "1", 'two': '2'}
        print(names ["three"])
    except KeyError:
        print("something")

def oops():
    try:
        [1,2][3]
    except IndexError:
        print("something again")    # я не понимаю, почему не выводится принт

