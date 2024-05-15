money_amount = list(map(int, input().split()))
prices = list(map(int, input().split()))

num_of_foods = 0

while money_amount and prices:
    current_money = money_amount.pop()
    current_price = prices.pop(0)

    if current_money == current_price:
        num_of_foods += 1

    elif current_money > current_price:
        num_of_foods += 1
        difference = current_money - current_price
        if money_amount:
            money_amount[-1] += difference

    else:
        continue

if num_of_foods >= 4:
    print(f'Gluttony of the day! Henry ate {num_of_foods} foods.')

elif num_of_foods > 1:
    print(f'Henry ate: {num_of_foods} foods.')

elif num_of_foods == 1:
    print(f'Henry ate: {num_of_foods} food.')

else:
    print('Henry remained hungry. He will try next weekend again.')
