number_of_companions = int(input())
days = int(input())
coins = 0

for current_day in range(1, days + 1):
    if current_day % 10 == 0:
        number_of_companions -= 2

    if current_day % 15 == 0:
        number_of_companions += 5

    if current_day % 3 == 0:
        coins -= number_of_companions * 3

    if current_day % 5 == 0:
        coins += number_of_companions * 20

        if current_day % 3 == 0:
            coins -= number_of_companions * 2

    coins += 50
    coins -= number_of_companions * 2

coins_per_companion = coins // number_of_companions

print(f"{number_of_companions} companions received {coins_per_companion} coins each.")
