table = set()

for _ in range(int(input())):
    for el in input().split():
        table.add(el)

print(*table, sep="\n")