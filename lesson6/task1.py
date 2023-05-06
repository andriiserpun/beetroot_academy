def largestnumber(numbers):

    biggest_num = numbers[0]

    for num in numbers:
        if num > biggest_num:
            biggest_num = num
    return biggest_num
print(largestnumber([473,45,8922,905940, 87, 2345]))