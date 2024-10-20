# TODO Найдите количество книг, которое можно разместить на дискете
pages = 100
rows_per_page = 50
chars_per_row = 25
char_size = 4 # байт
disk_size = 1.44 # Мб
disk_size_bytes = disk_size*1024*1024
book_size = pages * rows_per_page * chars_per_row * char_size
books_count = disk_size_bytes // book_size

print("Количество книг, помещающихся на дискету:", int(books_count))
