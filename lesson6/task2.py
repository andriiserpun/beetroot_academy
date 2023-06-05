import random
list1 = []
i = 0
while i < 10:
    num = random.randint(1, 10)
    list1.append(num)
    i += 1
list2 = []
i = 0
while i < 10:
    num = random.randint(1, 10)
    list2.append(num)
    i += 1
common_numbers = []
i = 0
while i < len(list1):
    if list1[i] in list2 and list1[i] not in common_numbers:
        common_numbers.append(list1[i])
    i += 1
print("List 1:", list1)
print("List 2:", list2)
print("Common Numbers:", common_numbers)