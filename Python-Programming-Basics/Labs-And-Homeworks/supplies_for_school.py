pen = int(input())
markers = int(input())
detergent = int(input())
discount_percent = int(input())

price_pen = pen * 5.80
price_markers = markers * 7.20
price_detergent = detergent * 1.20

total_price = price_pen + price_markers + price_detergent
discount = total_price * discount_percent / 100
sum_discount = total_price - discount

print(sum_discount)
