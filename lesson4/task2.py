def get_string (text):
    if len(text) < 9:
        return "False"
    if len(text) > 10:
        return "False"
    if len(text) >= 10:
        return "True"
my_string = input("Phone number: ")
print("New modified string is : ", get_string(my_string))