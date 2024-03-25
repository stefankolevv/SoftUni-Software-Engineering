book = input()

count = 0
is_found = False
input_line = input()
while input_line != "No More Books":
    if input_line == book:
        is_found = True
        break

    count = count + 1
    input_line = input()

if is_found:
    print(f"You checked {count} books and found it.")
else:
    print("The book you search is not here!")
    print(f"You checked {count} books.")