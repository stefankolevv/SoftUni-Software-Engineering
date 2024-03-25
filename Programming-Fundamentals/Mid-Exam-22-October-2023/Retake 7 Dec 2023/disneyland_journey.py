journey_cost = float(input())
months = int(input())

saved_money = 0

for month in range(1, months + 1):
    saved_money += journey_cost * 0.25

    if month % 2 != 0 and month != 1:
        spent_money = saved_money * 0.16
        saved_money -= spent_money

    if month % 4 == 0:
        bonus = saved_money * 0.25
        saved_money += bonus

if saved_money >= journey_cost:
    money_left = saved_money - journey_cost
    print(f"Bravo! You can go to Disneyland and you will have {money_left:.2f}lv. for souvenirs.")
else:
    money_needed = journey_cost - saved_money
    print(f"Sorry. You need {money_needed:.2f}lv. more.")

