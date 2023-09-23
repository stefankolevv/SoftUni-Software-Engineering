num = int(input())
left_sum = 0
right_sum = 0

for number in range(0, num * 2):
    current_num = int(input())
    if number < num:
        left_sum += current_num
    elif number >= num:
        right_sum += current_num

if left_sum == right_sum:
    print(f"Yes, sum = {left_sum}")
else:
    diff = abs(left_sum - right_sum)
    print(f"No, diff = {diff}")
