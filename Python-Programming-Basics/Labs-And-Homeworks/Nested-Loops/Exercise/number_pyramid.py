number = int(input())

flag = False
current_number = 1
for row in range(1, number + 1):
    for col in range(1, row + 1):
        if current_number > number:
            flag = True
            break

        print(current_number, end=" ")

        current_number += 1
    print()
    if flag:
        break
