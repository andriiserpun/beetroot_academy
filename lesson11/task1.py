    # первый скрипт для создания файла
filename = "myfile.txt"
with open("myfile.txt", "w") as file:
    file.write("Hello file World!")
    # второй скрипт для чтения файла
with open("myfile.txt", "r") as file:
    content = file.read()
print(content)