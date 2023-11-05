def calculate_total_price(product, quantity):
    if product == "coffee":
        return f"{1.50 * quantity:.2f}"
    elif product == "coke":
        return f"{1.40 * quantity:.2f}"
    if product == "water":
        return f"{1.00 * quantity:.2f}"
    if product == "snacks":
        return f"{2.00 * quantity:.2f}"

product = input()
quantity = int(input())
result = calculate_total_price(product, quantity)
print(result)
