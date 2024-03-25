age = int(input())
type_of_drink = ""

if age <= 14:
    type_of_drink = "toddy"
elif age <= 18:
    type_of_drink = "coke"
elif age <= 21:
    type_of_drink = "beer"
else:
    type_of_drink = "whisky"

print(f"drink {type_of_drink}")