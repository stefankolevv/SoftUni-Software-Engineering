number = input()

sorted_number = ''.join(sorted(number, reverse=True))
result = int(sorted_number)

print(result)
