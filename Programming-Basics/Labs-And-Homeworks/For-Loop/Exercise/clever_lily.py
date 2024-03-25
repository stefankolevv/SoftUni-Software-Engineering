age = int(input())
washing_machine_price = float(input())
toy_price = int(input())

toys_counter = 0
saved_money = 0
money_in_brother = 0

for year in range(1, age + 1):
    if year % 2 == 0:
        saved_money += int(year / 2) * 10
        money_in_brother += 1
    else:
        toys_counter += 1

money_from_toys = toys_counter * toy_price
total_saved_money = money_from_toys + saved_money - money_in_brother

diff_money = abs(total_saved_money - washing_machine_price)

if total_saved_money >= washing_machine_price:
    print(f"Yes! {diff_money:.2f}")
else:
    print(f"No! {diff_money:.2f}")