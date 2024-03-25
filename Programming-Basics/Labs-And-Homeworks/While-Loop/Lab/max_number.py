import sys

input_line = input()
max_number = -sys.maxsize

while input_line != "Stop":
    current_number = int(input_line)

    if current_number > max_number:
        max_number = current_number

    input_line = input()

print(max_number)