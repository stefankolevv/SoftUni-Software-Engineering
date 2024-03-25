cards_input_line = input().split(":")
new_deck = []

while True:
    command = input().split()

    if command[0] == "Ready":
        break

    action = command[0]
    name_of_the_card = command[1]

    if action == "Add":
        if name_of_the_card in cards_input_line:
            new_deck.append(name_of_the_card)
        else:
            print("Card not found.")

    elif action == "Insert":
        index = int(command[2])
        if name_of_the_card in cards_input_line and 0 <= index < len(new_deck):
            new_deck.insert(index, name_of_the_card)
        else:
            print("Error!")

    elif action == "Remove":
        if name_of_the_card in new_deck:
            new_deck.remove(name_of_the_card)
        else:
            print("Card not found.")

    elif action == "Swap":
        name_of_the_card2 = command[2]
        index1 = new_deck.index(name_of_the_card)
        index2 = new_deck.index(name_of_the_card2)
        new_deck[index1], new_deck[index2] = new_deck[index2], new_deck[index1]

    elif action == "Shuffle":
        new_deck.reverse()

print(" ".join(new_deck))