input_numbers = input()
numbers_list = [int(num) for num in input_numbers.split()]

minimum_number = min(numbers_list)
maximum_number = max(numbers_list)
sum_of_numbers = sum(numbers_list)

print(f"The minimum number is {minimum_number}")
print(f"The maximum number is {maximum_number}")
print(f"The sum number is: {sum_of_numbers}")
