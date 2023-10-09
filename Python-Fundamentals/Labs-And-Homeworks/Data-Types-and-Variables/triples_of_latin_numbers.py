number_of_symbols = int(input())

for first_symbol in range(number_of_symbols):
    for second_symbol in range(number_of_symbols):
        for third_symbol in range(number_of_symbols):
            print(f"{chr(97 + first_symbol)}{chr(97 + second_symbol)}{chr(97 + third_symbol)}")
