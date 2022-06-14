from dataclasses import dataclass


@dataclass
class Book:
    title: str
    content: str
    author: str


books = [
    Book("Pan Tadeusz", "ccc", "Adam Mickiewicz"),
    Book("Krzyżacy", "ccc", "Henryk Sienkiewicz"),
]


@dataclass
class Author:
    name: str
    last_name: str


authors = [
    Author("Adam", "Mickiewicz"),
    Author("Henryk", "Sienkiewicz")

]
