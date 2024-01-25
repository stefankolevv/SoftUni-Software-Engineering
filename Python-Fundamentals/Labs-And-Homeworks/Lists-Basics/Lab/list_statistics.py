n = int(input())

positive_numbers = []
negative_numbers = []

for _ in range(n):
    number = int(input())

    if number >= 0:
        positive_numbers.append(number)
    else:
        negative_numbers.append(number)

print(positive_numbers)
print(negative_numbers)
print("Count of positives:", len(positive_numbers))
print("Sum of negatives:", sum(negative_numbers))
