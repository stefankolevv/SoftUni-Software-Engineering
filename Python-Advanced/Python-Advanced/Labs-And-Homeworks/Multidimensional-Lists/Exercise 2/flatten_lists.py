numbers = [string.split() for string in input().split("|")]
print(*[' '.join(sub_list) for sub_list in numbers[::-1] if sub_list])