number_of_people = int(input())
lift_state = [int(wagon) for wagon in input().split()]

for i in range(len(lift_state)):
    while lift_state[i] < 4 and number_of_people > 0:
        lift_state[i] += 1
        number_of_people -= 1

lift_full = all(wagon == 4 for wagon in lift_state)

if number_of_people == 0 and not lift_full:
    print("The lift has empty spots!")
elif number_of_people > 0 and lift_full:
    print(f"There isn't enough space! {number_of_people} people in a queue!")
print(" ".join(map(str, lift_state)))
