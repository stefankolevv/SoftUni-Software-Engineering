items = input().split('|')
budget = int(input())
bought_items = []

for i in items:
    item = i.split('->')
    valid = False
    item_price = float(item[1])

    if item[0] == 'Clothes' and item_price <= 50:
        valid = True
    elif item[0] == 'Shoes' and item_price <= 35:
        valid = True
    elif item[0] == 'Accessories' and item_price <= 20.50:
        valid = True

    if valid:
        if budget - item_price < 0:
            break

        budget -= item_price
        bought_items.append(item_price)

items_with_profit = [item * 1.4 for item in bought_items]

for item in items_with_profit:
    print(f'{item:.2f}', end=' ')

print()
print(f'Profit: {abs(sum(bought_items) - sum(items_with_profit)):.2f}')
if sum(items_with_profit) + budget >= 150:
    print('Hello, France!')
else:
    print('Not enough money.')
