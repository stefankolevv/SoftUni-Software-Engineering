start_interval = int(input())
final_interval = int(input())
magic_number = int(input())

combination_counter = 0
break_condition = False

for x in range(start_interval, final_interval + 1):
    for y in range(start_interval, final_interval + 1):

        combination_counter += 1

        if x + y == magic_number:
            print(f"Combination N:{combination_counter} ({x} + {y} = {magic_number})")
            break_condition = True
            break

    if break_condition:
        break

else:
    print(f"{combination_counter} combinations - neither equals {magic_number}")