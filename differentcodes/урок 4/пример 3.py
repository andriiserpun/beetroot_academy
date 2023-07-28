while True:
    value = input('Введите значение 1 (Фаренгейт) или 2 (Цельсий): ')
    if value == '1':
        C = input('Введите температуру: ')
        F = int(C) * 1.8 + 32
        print(f'Значение по Фаренгейту: {F}')
    elif value == '2':
        F = input('Введите температуру: ')
        C = (int(F) - 32) / 1.8
        print(f'Значение по Цельсию: {C}')
    elif value == 'q':
        break
    else:
        print('Неверное значение')