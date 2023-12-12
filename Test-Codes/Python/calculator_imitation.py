command = input('Enter a command: ')
available_commands = ['+', '-', '*', '/', '%', '**', '//']

if command not in available_commands:
    print('Error message: Invalid command! Try one of these instead...')
    print(', '.join(available_commands))
else:
    if command == '+':
        add = lambda num1, num2: num1 + num2
        result = add(*map(float, input("Enter numbers: ").split()))
        print(f'Result \'adding\': {result:.2f}')

    elif command == '-':
        subtract = lambda num1, num2: num1 - num2
        result = subtract(*map(float, input("Enter numbers: ").split()))
        print(f'Result \'subtracting\': {result:.2f}')

    elif command == '*':
        multiply = lambda num1, num2: num1 * num2
        result = multiply(*map(float, input("Enter numbers: ").split()))
        print(f'Result \'multiplication\': {result:.2f}')

    elif command == '/':
        division = lambda num1, num2: num1 / num2
        result = division(*map(float, input("Enter numbers: ").split()))
        print(f'Result \'division\': {result:.2f}')

    elif command == '%':
        modulus = lambda num1, num2: num1 % num2
        result = modulus(*map(float, input("Enter numbers: ").split()))
        print(f'Result \'modulus\': {result:.2f}')

    elif command == '**':
        exponentiation = lambda num1, num2: num1 ** num2
        result = exponentiation(*map(float, input("Enter numbers: ").split()))
        print(f'Result \'exponentiation\': {result:.2f}')

    elif command == '//':
        floor_division = lambda num1, num2: num1 // num2
        result = floor_division(*map(float, input("Enter numbers: ").split()))
        print(f'Result \'floor division\': {result:.2f}')
