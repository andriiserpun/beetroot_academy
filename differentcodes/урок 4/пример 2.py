words = input("Введіть текст:\t")
sum_digits = 0
i = 0
while i < len(words):
    if words[i].isdigit():
        sum_digits += int(words[i])
    i += 1
print(f"Сума чисел: {sum_digits}")