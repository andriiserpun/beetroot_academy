try:
    a = input("Write the number a: ")
    b = input("write the number b: ")
    if b == 0:
        raise ZeroDivisionError
    return (a**2) / b
except (ZeroDivisionError, ValueError):
    print("sorry, something went wrong")
    ef

