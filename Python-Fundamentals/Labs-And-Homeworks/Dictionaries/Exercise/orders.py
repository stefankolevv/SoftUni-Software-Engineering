products = {}

while True:
    input_line = input()
    if input_line == "buy":
        break

    name, price, quantity = input_line.split()
    price = float(price)
    quantity = int(quantity)

    if name not in products:
        products[name] = {"price": price, "quantity": quantity}
    else:
        products[name]["price"] = price
        products[name]["quantity"] += quantity

for product, data in products.items():
    total_price = data["price"] * data["quantity"]
    print(f"{product} -> {total_price:.2f}")
