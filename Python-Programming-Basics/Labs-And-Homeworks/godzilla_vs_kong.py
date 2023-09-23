budget = float(input())
statists = int(input())
clothing_price = float(input())

decor_price = budget * 0.1
all_clothes = statists * clothing_price

if statists > 150:
    all_clothes = all_clothes * 0.90

total = decor_price + all_clothes

diff = abs(budget - total)
if budget >= total:
    print("Action!")
    print(f"Wingard starts filming with {diff:.2f} leva left.")
else:
    print("Not enough money!")
    print(f"Wingard needs {diff:.2f} leva more.")
