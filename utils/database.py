"""
Concerned with storing and retrieving books from a json file.
Format of the json file:

 [
    {
      "name": "The Lord of The Rings",
      "author": "J.R.R Tolkiem",
      "read": False
    },
    {
      "name": "The Hobbit",
      "author": "J.R.R Tolkiem",
      "read": True
    },
    {
      "name": "1984",
      "author": "George Orwell",
      "read": False
    }
]

"""
import json


def create_book_file():
    with open('books.json', 'w') as file:
        json.dump([], file)


def add_book(name, author):
    books = get_all_books()
    books.append({"name": name, "author": author, "read": False})
    _save_all_books(books)


def get_all_books():
    with open('books.json', 'r') as file:
        return json.load(file)



def _save_all_books(books):
    with open('books.json', 'w') as file:
        json.dump(books, file)


def mark_book_as_read(name):
    books = get_all_books()

    for book in books:
        if book["name"] == name:
            book["read"] = True

    _save_all_books(books)


def delete_book(name):
    books = get_all_books()
    books = [book for book in books if book["name"] != name]
    _save_all_books(books)