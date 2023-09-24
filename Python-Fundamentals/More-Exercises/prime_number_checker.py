number = int(input())

if number < 2:
    is_prime = False
else:
    is_prime = True

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            is_prime = False
            break

print(is_prime)
