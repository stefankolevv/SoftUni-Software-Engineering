budget = float(input())
flour = float(input())

egg_price_per_pack = 0.75 * flour
milk_price_per_liter = 1.25 * flour
milk_price_per_250ml = milk_price_per_liter / 4

eggs_collected = 0
loaves = 0

while budget >= flour:
    budget -= (flour + egg_price_per_pack + milk_price_per_250ml)
    eggs_collected += 3
    loaves += 1
    if loaves % 3 == 0:
        eggs_collected -= (loaves - 2)

money_left = '{:.2f}'.format(budget)
eggs_collected = str(eggs_collected)

print(f"You made {loaves} loaves of Easter bread! Now you have {eggs_collected} eggs and {money_left}BGN left.")
