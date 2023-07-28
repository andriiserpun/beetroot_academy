def str_read(text):
    return text
def int_read(number):
    if number.isdigit():
        return int(number)
    else:
        print("Error")
        return None
def float_read(number):
    number_without_point = number.replace(".", "")
    if number_without_point.isdigit() and "." in number and number.count(".") == 1:
        return float(number)
    else:
        print("Error")
        return None
def text_read(text):
    text = text.replace(".",",,").replace(",",",,").replace("-",",,")
    return text.split(",,")
def numbers_read(numbers):
    numbers = numbers.split(",")
    result = []
    for i in numbers:
        if '.' in i and i.count(".") == 1:
            number = float_read(i)
        else:
            number = int_read(i)
        result.append(number)
    return result