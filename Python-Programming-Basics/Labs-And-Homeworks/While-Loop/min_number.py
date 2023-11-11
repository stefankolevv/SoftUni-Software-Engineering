import sys

input_line = input()
min_number = sys.maxsize

while input_line != "Stop":
    current_number = int(input_line)

    if current_number < min_number:
        min_number = current_number

    input_line = input()

print(min_number)
