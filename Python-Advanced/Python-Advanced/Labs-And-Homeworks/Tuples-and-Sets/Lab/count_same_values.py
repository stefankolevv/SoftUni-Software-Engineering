numbers = tuple([float(el) for el in input().split()])

same_values = {}

for num in numbers:
    if num not in same_values:
        same_values[num] = numbers.count(num)

for number, occ in same_values.items():
    print(f'{number} - {occ} times')