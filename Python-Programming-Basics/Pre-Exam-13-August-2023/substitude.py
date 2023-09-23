K = int(input())
L = int(input())
M = int(input())
N = int(input())

valid_swaps = 0

for num1_digit1 in range(K, 9):
    for num1_digit2 in range(9, L - 1, -1):
        for num2_digit1 in range(M, 9):
            for num2_digit2 in range(9, N - 1, -1):
                if num1_digit1 % 2 == 0 and num1_digit2 % 2 != 0 and \
                   num2_digit1 % 2 == 0 and num2_digit2 % 2 != 0:
                    num1 = str(num1_digit1) + str(num1_digit2)
                    num2 = str(num2_digit1) + str(num2_digit2)
                    if num1_digit1 == num2_digit1 and num1_digit2 == num2_digit2:
                        print("Cannot change the same player.")
                    elif num1 != num2:
                        print(f"{num1} - {num2}")
                        valid_swaps += 1
                        if valid_swaps == 6:
                            exit()
