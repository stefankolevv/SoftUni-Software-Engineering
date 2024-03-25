journey_costs = float(input())
months = int(input())

total_saved_money = 0

for month in range(1, months + 1):
    if month > 1 and month % 2 == 1:
        expenses = total_saved_money * 0.16
        total_saved_money -= expenses

    total_saved_money += (journey_costs * 0.25)

    if month % 4 == 0:
        bonus = total_saved_money * 0.25
        total_saved_money += bonus

money_left = total_saved_money - journey_costs

if money_left >= 0:
    print(f"Bravo! You can go to Disneyland and you will have {money_left:.2f}lv. for souvenirs.")
else:
    needed_money = abs(money_left)
    print(f"Sorry. You need {needed_money:.2f}lv. more.")