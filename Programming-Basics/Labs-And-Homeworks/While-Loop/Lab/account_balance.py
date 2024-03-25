available_account_sum = 0

while True:
    data = input()

    if data == "NoMoreMoney":
        break

    current_sum = float(data)

    if current_sum >= 0:
        available_account_sum += current_sum
        print(f"Increase: {current_sum:.2f}")
    else:
       print("Invalid operation!")
       break

print(f"Total: {available_account_sum:.2f}")