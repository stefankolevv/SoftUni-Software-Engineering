days = int(input())
type_room = input()
rate = input()

days_rent = days - 1

price = 0

if type_room == "room for one person":
    price = 18
elif type_room == "apartment":
    price = 25
    if days > 15:
        price *= 0.50
    elif days >= 10:
        price *= 0.65
    else:
        price *= 0.70
elif type_room == "president apartment":
    price = 35
    if days > 15:
        price *= 0.80
    elif days >= 10:
        price *= 0.85
    else:
        price *= 0.90

if rate == "positive":
    price *= 1.25
elif rate == "negative":
    price *= 0.90

total_price = price * days_rent

print(f"{total_price:.2f}")
