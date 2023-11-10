def all_the_characters(first_char: str, second_char: str) -> list:
    characters = []
    for current_character_as_digit in range(ord(first_char) + 1, ord(second_char)):
        characters.append(chr(current_character_as_digit))
    return characters


first_character = input()
second_character = input()
final_result = all_the_characters(first_character, second_character)
print(" ".join(final_result))
