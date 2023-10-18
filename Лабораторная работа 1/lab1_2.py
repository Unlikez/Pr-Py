disk_size = 1.44 * 1024 * 1024  # байт
num_pages = 100
num_str = 50
num_symb = 25
symb_size = 4

book_size = num_pages * num_str * num_symb * symb_size
num_books = int(disk_size // book_size)
print("Количество книг, помещающихся на дискету:", num_books)
