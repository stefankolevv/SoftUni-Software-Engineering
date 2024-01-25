deposit = float(input())
months = int(input())
annual_rate = float(input())

per_year = deposit * annual_rate / 100
per_month = per_year / 12
total = deposit + months * per_month

print(total)
