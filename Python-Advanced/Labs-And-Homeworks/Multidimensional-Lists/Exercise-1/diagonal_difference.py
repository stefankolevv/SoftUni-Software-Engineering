num = int(input())

primary_sum, secondary_sum = 0, 0

for i in range(num):
    line = [int(x) for x in input().split()]
    primary_sum += line[i]
    secondary_sum += line[num - i - 1]

print(abs(primary_sum - secondary_sum))
