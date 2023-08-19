def calculate_square_division():
    try:
        a = float(input("Введите значение a: "))
        b = float(input("Введите значение b: "))

        result = (a ** 2) / b

        if b == 0:
            raise ZeroDivisionError("Деление на ноль недопустимо")

        return result

    except ValueError:
        print("Ошибка: Введите числовые значения для a и b")
    except ZeroDivisionError as e:
        print(f"Ошибка: {e}")


result = calculate_square_division()
if result is not None:
    print(f"Результат: {result}")
