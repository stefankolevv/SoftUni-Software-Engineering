chicken_menu = int(input())
fish_menu = int(input())
vegetarian_menu = int(input())

price_chicken_menu = chicken_menu * 10.35
price_fish_menu = fish_menu * 12.4
price_vegetarian_menu = vegetarian_menu * 8.15

all_menu = price_chicken_menu + price_fish_menu + price_vegetarian_menu
dessert_price = all_menu * 0.20

order_price = all_menu + dessert_price + 2.50

print(order_price)