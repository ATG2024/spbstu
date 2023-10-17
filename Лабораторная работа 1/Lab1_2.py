# TODO Найдите количество книг, которое можно разместить на дискете
symbol_ = 4
quant_symbol_line = 25
quant_line_page = 50
quant_page_book = 100
disk_ = 1.44
allByte = symbol_ * quant_symbol_line *quant_line_page * quant_page_book
quant_book_in_disk = int(disk_ * 1024 * 1024 // allByte)
print("Количество книг, помещающихся на дискету:", quant_book_in_disk)
