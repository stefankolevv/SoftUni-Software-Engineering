def process_string(s):
    total_sum = 0

    for substring in s.split():
        first_letter = substring[0]
        last_letter = substring[-1]
        number = int(substring[1:-1])

        if first_letter.isupper():
            position = ord(first_letter) - ord('A') + 1
            number /= position
        else:
            position = ord(first_letter) - ord('a') + 1
            number *= position

        if last_letter.isupper():
            position = ord(last_letter) - ord('A') + 1
            number -= position
        else:
            position = ord(last_letter) - ord('a') + 1
            number += position

        total_sum += number

    return total_sum


input_string = input()
result = process_string(input_string)
print(f'{result:.2f}')
