animals = input().split(', ')

if animals[-1] == 'wolf':
    print("Please go away and stop eating my sheep")

else:
    wolf_index = animals.index('wolf')
    sheep_number = len(animals) - wolf_index - 1
    print(f"Oi! Sheep number {sheep_number}! You are about to be eaten by a wolf!")
