# SOLUTION 1
star_len = int(input("Введіть довжину вершини:\t"))
i = 1
while i < star_len:
    print('* '*i)
    i += 1
while i > 0:
    print('* '*i)
    i -= 1
# SOLUTION 2
# star_len = int(input("Введіть довжину вершини:\t"))
# i = 0
# while i < star_len * 2:
#     if i < star_len:
#         print("* " * (i + 1))
#     elif i == star_len:
#         i += 1
#         continue
#     else:
#         print("* " * (star_len * 2 - i))
#     i += 1
# SOLUTION 3
# star_len = int(input("Введіть довжину вершини:\t"))
# i = 1
# up = True
# while i != 0:
#     if i < star_len and up:
#         print("* " * i)
#         i += 1
#     elif i == star_len and up:
#         up = False
#         print("* " * i)
#     else:
#         i -= 1
#         print("* " * i)