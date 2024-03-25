numbers_as_string = input().split()
numbers_as_digits = []

for number in numbers_as_string:
    numbers_as_digits.append(int(number))

is_even = lambda x: x % 2 == 0
result = list(filter(is_even, numbers_as_digits))
print(result)