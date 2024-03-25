num_pages = int(input())
pages_per_hour = int(input())
num_days = int(input())

total_hours = num_pages // pages_per_hour
hours_day = total_hours // num_days

print(hours_day)