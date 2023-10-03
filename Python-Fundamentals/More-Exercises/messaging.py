numbers_sequence = input().split()
numbers = [int(num) for num in numbers_sequence]

text = input()

message = []

for number in numbers:
    index = 0
    while number > 0:
        index += number % 10
        number //= 10

    while index >= len(text):
        index -= len(text)

    message.append(text[index])
    text = text[:index] + text[index+1:]

print("".join(message))
