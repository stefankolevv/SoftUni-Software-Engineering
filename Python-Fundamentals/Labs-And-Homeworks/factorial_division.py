def calculate_the_factorial(number):
    for current_number in range(1, number):
        number *= current_number
    return number  # initial number factorial -> number!
 
 
first_number = int(input())
second_number = int(input())
first_number_factorial = calculate_the_factorial(first_number)
second_number_factorial = calculate_the_factorial(second_number)
result = first_number_factorial / second_number_factorial
print(f"{result:.2f}")
