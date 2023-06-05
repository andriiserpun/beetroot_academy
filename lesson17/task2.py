class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.authors = []
    def new_book(self, name, year, author):
        book = Book(name, year, author)
        self.books.append(book)
        author.add_book(book)
        return book
    def group_by_author(self, author):
        return [book for book in self.books if book.author == author]
    def group_by_year(self, year):
        return [book for book in self.books if book.year == year]
    def __repr__(self):
        return f"Library: name - {self.name}, books - {self.books}, authors - {self.authors}"
    def __str__(self):
        return self.name
class Book:
    total_books = 0
    def __init__(self, name, year, author):
        self.name = name
        self.year = year
        self.author = author
        Book.total_books += 1

    def __repr__(self):
        return f"Library: name - {self.name}, books - {self.books}, authors - {self.authors}"
    def __str__(self):
        return self.name
class Author:
    def __init__(self, name, country, birthday):
        self.name = name
        self.country = country
        self.birthday = birthday
        self.books = []

    def add_book(self, book):
        self.books.append(book)
    def __repr__(self):
        return f"Author: name - {self.name}, country - {self.country}, birthday - {self.birthday}, books - {self.books}"
    def __str__(self):
        return self.name

author1 = Author("Fedor Dostoyevsky", "Russian Empire", "1821-11-11")
author2 = Author("Ivan Franko", "Ukraine (Austrian Empire)", "1856-08-27")

library = Library("My library")

book1 = library.new_book("Anna Karenina", 1878, author1)
book2 = library.new_book("Zakhar Berkut", 1883, author2)

author1_books = library.group_by_author(author1)
author2_books = library.group_by_author(author2)

author1_books = library.group_by_author(author1)
author2_books = library.group_by_author(author2)

print(library)

print("Books by Author 1:")
for book in author1_books:
    print(book)

print("Books by Author 2:")
for book in author2_books:
    print(book)

print("Total number of books:", Book.total_books)
# class Book:
#     pass
# class Author:
#     pass
