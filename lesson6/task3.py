initial_list = list(range(1, 100))
result_list = []
i = 0
while i < len(initial_list):
    num = initial_list[i]
    if num % 7 == 0 and num % 5 != 0:
        result_list.append(num)
    i += 1
print(result_list)