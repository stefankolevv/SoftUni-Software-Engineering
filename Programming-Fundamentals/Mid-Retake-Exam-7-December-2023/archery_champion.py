targets = list(map(int, input().split("|")))
points = 0

while True:
    cmd_input_line = input()

    if cmd_input_line == "Game over":
        break

    tokens = cmd_input_line.split("@")
    action = tokens[0]

    if action == "Shoot Left":
        start_index = int(tokens[1])
        length = int(tokens[2])
        if 0 <= start_index < len(targets):
            index = (start_index - length) % len(targets)
            if targets[index] >= 5:
                points += 5
                targets[index] -= 5
            else:
                points += targets[index]
                targets[index] = 0

    elif action == "Shoot Right":
        start_index = int(tokens[1])
        length = int(tokens[2])
        if 0 <= start_index < len(targets):
            index = (start_index + length) % len(targets)
            if targets[index] >= 5:
                points += 5
                targets[index] -= 5
            else:
                points += targets[index]
                targets[index] = 0

    elif action == "Reverse":
        targets.reverse()

print(" - ".join(map(str, targets)))
print(f"John finished the archery tournament with {points} points!")