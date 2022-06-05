wanted_book = input()
input_line = input()
book_counter = 0
while input_line != 'No More Books':
    if wanted_book == input_line:
        break
    book_counter += 1
    input_line = input()
if wanted_book == input_line:
    print(f'You checked {book_counter} books and found it.')
else:
    print(f'The book you search is not here!')
    print(f'You checked {book_counter} books.')
