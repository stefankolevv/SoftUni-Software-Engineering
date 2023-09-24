key = int(input())
n = int(input())

message = ""

for _ in range(n):
    char = input()
    decoded_char = chr(ord(char) + key)
    message += decoded_char

print(message)
