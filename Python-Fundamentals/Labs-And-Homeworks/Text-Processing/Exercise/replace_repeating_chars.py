text = input()
final_message = ""
last_added_character = ""
for current_character in text:
    if current_character != last_added_character:
        final_message += current_character
        last_added_character = current_character
print(final_message)
