import json
from book_store.models import *
from django.http import HttpResponse
import asyncio
from asgiref.sync import sync_to_async

# async def load_authors(filename):
#     with open(filename, "r") as file:
#         data = json.load(file)
#
#     for record in data:
#         await Author.objects.acreate(**record)
#
#
# async def load_books(filename):
#     with open(filename, "r") as file:
#         data = json.load(file)
#
#     for record in data:
#         authors_data = record.pop("authors")
#         await Book.objects.acreate(**record)
#
#         authors = []
#         for author_record in authors_data:
#             print("AUTHOR RECORD", author_record)
#             author = Author.objects.aget_or_create(id=author_record)
#             authors.append(author)


def load_authors_sync(filename):
    with open(filename, "r") as file:
        data = json.load(file)

    for record in data:
        Author.objects.create(**record)


def load_books_sync(filename):
    with open(filename, "r") as file:
        data = json.load(file)

    for record in data:
        authors_data = record.pop("authors", [])
        book = Book.objects.create(**record)

        authors = []
        for author_record in authors_data:
            print("AUTHOR RECORD", author_record)
            author = Author.objects.get_or_create(id=author_record)
            authors.append(author)
        print("BOOK.AUTHORS", book.authors)
        print("AUTHORS", authors)
        for author in authors:
            print("AUTTHOR [0]]", author[0].id)
            book.authors.set(author)



async def load_data():
    await asyncio.gather(
        sync_to_async(load_authors_sync)('book_store/input_files/authors.json'),
        sync_to_async(load_books_sync)('book_store/input_files/books.json'))
    return "Book store data have been uploaded into database"

async def async_load_data(request):
    await load_data()
    return HttpResponse('Book_store data were populated')
