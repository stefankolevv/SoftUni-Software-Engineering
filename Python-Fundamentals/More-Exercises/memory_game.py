elements = input().split()
moves = 0

while True:
    command = input()
    if command == "end":
        break

    i, j = map(int, command.split())

    if i == j or i < 0 or i >= len(elements) or j < 0 or j >= len(elements):
        print("Invalid input! Adding additional elements to the board")
        middle = len(elements) // 2
        elements.insert(middle, f"-{moves}a")
        elements.insert(middle, f"-{moves}a")
    else:
        if elements[i] == elements[j]:
            element = elements[i]
            elements = [el for el in elements if el != element]
            print(f"Congrats! You have found matching elements - {element}!")
        else:
            print("Try again!")

    moves += 1

if not elements:
    print(f"You have won in {moves} turns!")
else:
    print(f"Sorry you lose :(\n{' '.join(elements)}")
