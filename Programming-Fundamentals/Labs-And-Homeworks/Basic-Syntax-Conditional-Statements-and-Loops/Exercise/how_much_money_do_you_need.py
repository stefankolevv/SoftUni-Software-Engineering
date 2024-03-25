coffee_counter = 0
command = input()

while command != "END":
    if command.lower() == "coding" \
            or command.lower() == "dog" \
            or command.lower() == "cat" \
            or command.lower() == "movie":
        if command.islower():
            coffee_counter += 1
        else:
            coffee_counter += 2
    command = input()

if coffee_counter > 5:
    print("You need extra sleep")
else:
    print(coffee_counter)