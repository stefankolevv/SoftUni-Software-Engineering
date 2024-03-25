year_tax = int(input())

shoes_price = year_tax - year_tax * 0.4
suit_price = shoes_price - shoes_price * 0.2
ball_price = suit_price / 4
accessories_price = ball_price / 5

total_price = shoes_price + suit_price + ball_price + accessories_price + year_tax

print(total_price)