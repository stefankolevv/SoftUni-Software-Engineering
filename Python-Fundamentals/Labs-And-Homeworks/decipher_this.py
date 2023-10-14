secret_message = input().split()
deciphered = []

for word in secret_message:
    ascii_char = [char for char in word if char.isdigit()]
    word_list = [char for char in word if char not in ascii_char]

    first_letter = chr(int(''.join(ascii_char)))
    word_list[0], word_list[-1] = word_list[-1], word_list[0]
    new_word = first_letter + ''.join(word_list)
    deciphered.append(new_word)

print(' '.join(deciphered))
