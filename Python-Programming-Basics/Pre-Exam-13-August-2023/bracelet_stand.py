pockets_of_tereza = float(input())
money_she_gets = float(input())
expenses_of_tereza = float(input())
price_of_gift = float(input())

saved_money_from_pockets = 5 * pockets_of_tereza
earned_money = 5 * money_she_gets
total_saved_money = saved_money_from_pockets + earned_money
all_saved_money = total_saved_money - expenses_of_tereza

if all_saved_money > price_of_gift:
    print(f"Profit: {all_saved_money:.2f} BGN, the gift has been purchased.")
else:
    needed_money = price_of_gift - all_saved_money
    print(f"Insufficient money: {needed_money:.2f} BGN.")
