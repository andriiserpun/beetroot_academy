def oops():
    raise IndexError("Индекс вышел за границы")
def catch_exception():
    try:
        oops()
    except IndexError as e:
        print(f"Поймано исключение: {e}")
    except KeyError as e:
        print(f"Поймано исключение KeyError: {e}")

print("Пример с IndexError:")
catch_exception()
def oops():
    raise KeyError("Такого ключа не существует")

print("\nПример с KeyError:")
catch_exception()


