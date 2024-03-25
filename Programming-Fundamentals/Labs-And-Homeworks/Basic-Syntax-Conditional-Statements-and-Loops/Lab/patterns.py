number = int(input())

for i in range(number):
    for j in range(number - i):
        print(end=" ")
    for j in range(i + 1):
        print("*", end="")
    print()

for i in range(number - 1, 0, -1):
    for j in range(number - i + 1):
        print(end=" ")
    for j in range(i):
        print("*", end="")
    print()