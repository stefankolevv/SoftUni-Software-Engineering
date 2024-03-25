names_of_the_coffees = input().split()
num_of_commands = int(input())

while True:
    command = input()
    coffee = input()
    string = input()
    num_of_the_coffeess = input()

    if command == f"Include {coffee}":
        num_of_commands.insert(command)

    if command == f"Remove {string} {num_of_the_coffeess}":
        if string == "first" or string == "last":
            command[1] = num_of_commands.remove(num_of_coffeess)
    else:
        continue

    if command == f"Prefer {coffee[1]} or {coffee[2]}":
        num_of_commands.insert(coffee[1], coffee[2])
        num_of_commands.pop(num_of_commands[1] + 1)
        num_of_commands.insert(num_of_commands[2], num_of_commands[1])
        num_of_commands.pop(num_of_commands[2] + 1)
    else:
        continue

    if command == "Reverse":
        num_of_commands.reverse()

print(f"Coffees: \
      {coffee1} {coffee2}")


