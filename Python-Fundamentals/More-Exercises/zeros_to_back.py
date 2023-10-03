numbers_str = input()

numbers = [int(num) for num in numbers_str.split(', ')]

non_zero_numbers = [num for num in numbers if num != 0]
zeroes = [0] * (len(numbers) - len(non_zero_numbers))

result = non_zero_numbers + zeroes

print(result)
