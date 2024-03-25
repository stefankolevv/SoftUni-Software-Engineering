input_line = input()

prime_sum = 0
non_prime_sum = 0
while input_line != "stop":
    current_number = int(input_line)

    if current_number < 0:
        print("Number is negative.")
        input_line = input()
        continue

    count = 0
    for i in range(1, current_number + 1):
        if current_number % i == 0:
            count += 1

    if count == 2:
        prime_sum += current_number
    else:
        non_prime_sum += current_number

    input_line = input()

print(f"Sum of all prime numbers is: {prime_sum}")
print(f"Sum of all non prime numbers is: {non_prime_sum}")