number_of_characters = int(input())
total_sum = 0

for character in range(number_of_characters):
    current_character = input()
    total_sum += ord(current_character)

print(f"The sum equals: {total_sum}")
