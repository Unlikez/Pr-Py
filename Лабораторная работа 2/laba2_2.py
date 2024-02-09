
BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


class Book:
    def __init__(self, id, name, pages):
        self.id = id
        self.name = name
        self.pages = pages
    # TODO написать класс Book
    def __repr__(self) -> str:
        return f"Book(id_={self.id}, name='{self.name}', pages={self.pages})"


class Library:
    def __init__(self, books=0):
        self.books = books # TODO написать класс Library

    def get_next_book_id(self):
        if self.books == 0:
            return 1
        else:
            id = len(list_books) + 1
            return id
    def get_index_by_book_id(self,l):
        for i, ver in enumerate(self.books): #Я не понимаю как реализовать этот метод. Не понимаю как обратиться к экземпляру(с определенным id) в списке.
            return i
        #if l not list_books:
           # raise ValueError("Книги с запрашиваемым id не существует")

if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
