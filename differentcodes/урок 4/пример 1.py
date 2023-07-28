option = input("Виберіть режим роботи:\n1 - Переведення цельсій в фаренгейт\n2 - Переведення фаренгейт в цельсій\n")
if option == '1':
    temperature = float(input("Введіть температуру в цельсій:\t"))
    result = temperature * 1.8 + 32
    print(f"Результат переведення з цельсій в фаренгейт: {result}")
elif option == '2':
    temperature = float(input("Введіть температуру в фаренгейт:\t"))
    result = (temperature - 32) / 1.8
    print(f"Результат переведення з фаренгейт в цельсій: {result}")
else:
    print("Некоректно введено дані.")