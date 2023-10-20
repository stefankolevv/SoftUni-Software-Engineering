total_price = 0

while True:
    price_input = input()

    if price_input == "special" or price_input == "regular":
        break

    price = float(price_input)

    if price <= 0:
        print("Invalid price!")
        continue

    total_price += price

if total_price == 0:
    print("Invalid order!")
else:
    taxes = total_price * 0.20

    final_price = total_price + taxes

    customer_type = input()
    if customer_type == "special":
        final_price *= 0.90

    print(f"Congratulations you've just bought a new computer! \
          Price without taxes: {total_price:.2f}$ \
          Taxes: {taxes:.2f}$ \
          ----------- \
          Total price: {final_price:.2f}$")
