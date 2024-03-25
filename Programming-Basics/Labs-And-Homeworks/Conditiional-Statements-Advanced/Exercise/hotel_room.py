month = input()
count_nights = int(input())

apartment_price = 0
studio_price = 0
if month == "May" or month == "October":
    apartment_price = 65 * count_nights
    studio_price = 50 * count_nights

elif month == "June" or month == "September":
    apartment_price = 68.7 * count_nights
    studio_price = 75.2 * count_nights

elif month == "July" or month == "August":
    apartment_price = 77 * count_nights
    studio_price = 76 * count_nights

if count_nights > 14 and (month == "May" or month == "October"):
    studio_price = studio_price * 0.70
elif count_nights > 7 and (month == "May" or month == "October"):
    studio_price = studio_price * 0.95
elif count_nights > 14 and (month == "June" or month == "September"):
    studio_price = studio_price * 0.8

if count_nights > 14:
    apartment_price = apartment_price * 0.9

print(f"Apartment: {apartment_price:.2f} lv.")
print(f"Studio: {studio_price:.2f} lv.")