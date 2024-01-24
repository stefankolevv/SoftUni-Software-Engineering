numbers = input().split()
numbers_list = []

for number in numbers:
    rounded_numbers = round(float(number))
    numbers_list.append(rounded_numbers)

print(numbers_list)
