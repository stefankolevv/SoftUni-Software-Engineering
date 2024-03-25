budget = float(input())
season = input()

destination = ""
place = ""
price = 0
if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        place = "Camp"
        price = budget * 0.3
    elif season == "winter":
        place = "Hotel"
        price = budget * 0.7

elif budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        place = "Camp"
        price = budget * 0.4
    elif season == "winter":
        place = "Hotel"
        price = budget * 0.8

elif budget > 1000:
    destination = "Europe"
    place = "Hotel"
    price = budget * 0.9

print(f"Somewhere in {destination}")
print(f"{place} - {price:.2f}")