hall_rent = int(input())

discount_statues = hall_rent * 0.3
price_statues = hall_rent - discount_statues
discount_catering = price_statues * 0.15
price_catering = price_statues - discount_catering
price_sounding = price_catering / 2

total = hall_rent + price_statues + price_catering + price_sounding

print(f"{total:.2f}")
