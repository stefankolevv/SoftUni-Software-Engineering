some_string = input()
final_string = ""
strength = 0
for index in range(len(some_string)):
    # We have explostion
    if strength > 0 and some_string[index] != ">":
        strength -= 1
    # We have explosion mark
    elif some_string[index] == ">":
        final_string += some_string[index]
        strength += int(some_string[index + 1])
    # We have no explosion -> normal character
    else:
        final_string += some_string[index]
print(final_string)