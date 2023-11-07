shelf_with_books = input().split("&")
command = input()

while command != "Done":
    book_name = input()

    if command == f"Add Book | {book_name}":
        shelf_with_books.insert(book_name)
    else:
        continue

    if command == f"Take Book | {book_name}":
        shelf_with_books.pop(book_name)
    else:
        continue

    if command == f"Swap Books | {book_name[1]} {book_name[2]}":
        shelf_with_books.insert(book_name[1], book_name[2])
        shelf_with_books.pop(book_name[1] + 1)
        shelf_with_books.insert(book_name[2], book_name[1])
        shelf_with_books.pop(book_name[2] + 1)
    else:
        continue

    if command == f"Insert Book | {book_name}":
        shelf_with_books.append(book_name)
    else:
        continue

    index = input()
    if command == f"Check Book | {index}":
        print(index)
    else:
        continue

    result = ", ".join([book_name for book_name in shelf_with_books])
    print(result)
