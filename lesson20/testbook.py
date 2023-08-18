import json
import os

class PhoneBook:
    def __init__(self, name):
        self.name = name
        self.contacts = {}

    def load_data(self):
        if os.path.exists(f'{self.name}.json'):
            with open(f'{self.name}.json', 'r') as file:
                self.contacts = json.load(file)

    def save_data(self):
        with open(f'{self.name}.json', 'w') as file:
            json.dump(self.contacts, file)

    def add_contact(self, contact):
        phone_number = contact.get('phone_number')
        if phone_number:
            self.contacts[phone_number] = contact
            print('Контакт добавлен.')
        else:
            print('Ошибка: Номер телефона обязателен.')

    def search_by_name(self, first_name):
        results = [contact for contact in self.contacts.values() if contact['first_name'] == first_name]
        self.print_results(results)

    def search_by_last_name(self, last_name):
        results = [contact for contact in self.contacts.values() if contact['last_name'] == last_name]
        self.print_results(results)

    def search_by_full_name(self, full_name):
        results = [contact for contact in self.contacts.values() if f"{contact['first_name']} {contact['last_name']}" == full_name]
        self.print_results(results)

    def search_by_phone_number(self, phone_number):
        contact = self.contacts.get(phone_number)
        if contact:
            self.print_results([contact])
        else:
            print('Контакт не найден.')



    def print_results(self, results):
        for contact in results:
            print(f"Имя: {contact['first_name']}")
            print(f"Фамилия: {contact['last_name']}")
            print(f"Номер телефона: {contact['phone_number']}")
            print(f"Город: {contact.get('city', '-')}")
            print(f"Область: {contact.get('state', '-')}")
            print("=" * 20)

    def delete_contact(self, phone_number):
        if phone_number in self.contacts:
            del self.contacts[phone_number]
            print('Контакт удален.')
        else:
            print('Контакт не найден.')

    def update_contact(self, phone_number, updated_data):
        if phone_number in self.contacts:
            self.contacts[phone_number].update(updated_data)
            print('Контакт обновлен.')
        else:
            print('Контакт не найден.')



def main():
    phone_book_name = input("Введите имя телефонной книги: ")
    phone_book = PhoneBook(phone_book_name)
    phone_book.load_data()

    while True:
        print("\nВыберите действие:")
        print("1. Добавить контакт")
        print("2. Поиск по имени")
        print("3. Поиск по фамилии")
        print("4. Поиск по полному имени")
        print("5. Поиск по номеру телефона")
        print("6. Удалить контакт")
        print("7. Обновить контакт")
        print("8. Выйти")

        choice = input()

        if choice == '1':
            contact = {
                'first_name': input("Введите имя: "),
                'last_name': input("Введите фамилию: "),
                'phone_number': input("Введите номер телефона: "),
                'city': input("Введите город: "),
                'state': input("Введите область: ")
            }
            phone_book.add_contact(contact)
        elif choice == '2':
            first_name = input("Введите имя для поиска: ")
            phone_book.search_by_name(first_name)
        elif choice == '3':
            last_name = input("Введите фамилию для поиска: ")
            phone_book.search_by_last_name(last_name)
        elif choice == '4':
            full_name = input("Введите полное имя для поиска: ")
            phone_book.search_by_full_name(full_name)
        elif choice == '5':
            phone_number = input("Введите номер телефона для поиска: ")
            phone_book.search_by_phone_number(phone_number)
        elif choice == '6':
            phone_number = input("Введите номер телефона для удаления: ")
            phone_book.delete_contact(phone_number)
        elif choice == '7':
            phone_number = input("Введите номер телефона для обновления: ")
            updated_data = {
                'first_name': input("Введите новое имя: "),
                'last_name': input("Введите новую фамилию: "),
                'phone_number': input("Введите новый номер телефона: "),
                'city': input("Введите новый город: "),
                'state': input("Введите новую область: ")
            }
            phone_book.update_contact(phone_number, updated_data)
        elif choice == '8':
            phone_book.save_data()
            print("Данные сохранены!")
            break
        else:
            print("Некорректный вариант. Попробуйте снова.")



if __name__ == "__main__":
    main()
