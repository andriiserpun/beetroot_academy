def get_string (text):
    if len(text) < 2:
        return ""
    return text[:2] + text[-2:]
my_string = input("Enter a string : ")
print("New modified string is : ", get_string(my_string))