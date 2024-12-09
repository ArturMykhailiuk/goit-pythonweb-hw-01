from abc import ABC, abstractmethod
from typing import List
import logging

# Налаштування логування
file_handler = logging.basicConfig(
    format=("%(asctime)s - %(name)s - %(levelname)s - %(message)s"),
    level=logging.INFO,
    handlers=[
        logging.FileHandler(".\\solid\\program.log", encoding="utf-8"),
        logging.StreamHandler(),
    ],
)
logger = logging.getLogger(__name__)


class Book:
    def __init__(self, title: str, author: str, year: int) -> None:
        self.title = title
        self.author = author
        self.year = year

    def __str__(self) -> str:
        return f"Title: {self.title}, Author: {self.author}, Year: {self.year}"


class LibraryInterface(ABC):
    @abstractmethod
    def add_book(self, book: Book) -> None:
        pass

    @abstractmethod
    def remove_book(self, title: str) -> None:
        pass

    @abstractmethod
    def show_books(self) -> List[Book]:
        pass

    @abstractmethod
    def find_book(self, title: str) -> bool:
        pass


class Library(LibraryInterface):
    def __init__(self) -> None:
        self.books: List[Book] = []

    def add_book(self, book: Book) -> None:
        self.books.append(book)

    def remove_book(self, title: str) -> None:
        self.books = [book for book in self.books if book.title != title]

    def show_books(self) -> List[Book]:
        return self.books

    def find_book(self, title: str) -> bool:
        return any(book.title == title for book in self.books)


class LibraryManager:
    def __init__(self, library: LibraryInterface) -> None:
        self.library = library

    def add_book(self, title: str, author: str, year: int) -> None:
        book = Book(title, author, year)
        self.library.add_book(book)
        logger.info(f"Book added: {book}")

    def remove_book(self, title: str) -> None:
        if self.library.find_book(title):
            self.library.remove_book(title)
            logger.info(f"Book removed: {title}")
        else:
            logger.info(f"Book with title '{title}' not found.")

    def show_books(self) -> None:
        books = self.library.show_books()
        if books:
            for book in books:
                logger.info(book)
        else:
            logger.info("No books available in the library.")


def main() -> None:
    library = Library()
    manager = LibraryManager(library)

    while True:
        command = input("Enter command (add, remove, show, exit): ").strip().lower()

        if command == "add":
            title = input("Enter book title: ").strip()
            author = input("Enter book author: ").strip()
            year = int(input("Enter book year: ").strip())
            manager.add_book(title, author, year)
        elif command == "remove":
            title = input("Enter book title to remove: ").strip()
            manager.remove_book(title)
        elif command == "show":
            manager.show_books()
        elif command == "exit":
            logger.info("Goodbye!")
            break
        else:
            print("Unknown command. Please try again.")


if __name__ == "__main__":
    main()
