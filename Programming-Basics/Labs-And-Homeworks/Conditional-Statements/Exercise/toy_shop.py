trip_price = float(input())
puzzle = int(input())
dolls = int(input())
teddy = int(input())
minions = int(input())
trucks = int(input())

total_sum = puzzle * 2.60 + dolls * 3 + teddy * 4.10 + minions * 8.20 + trucks * 2

total_count = puzzle + dolls + teddy + minions + trucks

if total_count >= 50:
    total_sum = total_sum - (total_sum * 0.25)

total_sum = total_sum - (total_sum * 0.1)

diff = abs(total_sum - trip_price)
if total_sum >= trip_price:
    print(f"Yes! {diff:.2f} lv left.")
else:
    print(f"Not enough money! {diff:.2f} lv needed.")