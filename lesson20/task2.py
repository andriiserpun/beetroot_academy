import unittest
import os
from unittest.mock import patch
from testbook import PhoneBook



class TestPhoneBook(unittest.TestCase):

    def setUp(self):
        self.phone_book = PhoneBook("test_phonebook")

    def tearDown(self):
        if os.path.exists("test_phonebook.json"):
            os.remove("test_phonebook.json")

    def test_add_contact(self):
        contact = {
            'first_name': 'John',
            'last_name': 'Doe',
            'phone_number': '1234567890',
            'city': 'Sample City',
            'state': 'Sample State'
        }
        self.phone_book.add_contact(contact)
        self.assertIn('1234567890', self.phone_book.contacts)

    def test_search_by_name(self):
        contact = {
            'first_name': 'John',
            'last_name': 'Doe',
            'phone_number': '1234567890',
            'city': 'Sample City',
            'state': 'Sample State'
        }
        self.phone_book.add_contact(contact)
        with patch('builtins.print') as mock_print:
            self.phone_book.search_by_name('John')
            mock_print.assert_called_with(
                "Имя: John\nФамилия: Doe\nНомер телефона: 1234567890\nГород: Sample City\nОбласть: Sample State\n====================")



if __name__ == "__main__":
    unittest.main()
