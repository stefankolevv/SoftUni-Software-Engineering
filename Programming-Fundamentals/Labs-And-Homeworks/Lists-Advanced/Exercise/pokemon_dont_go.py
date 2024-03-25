sequence = [int(element) for element in input().split()]
points = 0

while len(sequence) != 0:
    index = int(input())
    num = 0
    if 0 <= index < len(sequence):
        num = sequence.pop(index)
    elif 0 > index:
        num_to_add = sequence[-1]
        num = sequence[0]
        sequence[0] = sequence[-1]
    else:
        num_to_add = sequence[0]
        num = sequence[-1]
        sequence[-1] = sequence[0]
    points += num
    for current_index, current_num in enumerate(sequence):
        if current_num <= num:
            sequence[current_index] += num
        else:
            sequence[current_index] -= num

print(points)