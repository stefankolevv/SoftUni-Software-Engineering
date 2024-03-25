budget = float(input())
videocards_count = int(input())
cpu_count = int(input())
ram_count = int(input())

videocards_sum = videocards_count * 250
cpu_sum = cpu_count * (videocards_sum * 0.35)
ram_sum = ram_count * (videocards_sum * 0.1)

total = videocards_sum + cpu_sum + ram_sum

if videocards_count > cpu_count:
    total = total * 0.85

diff = abs(total - budget)
if budget >= total:
    print(f"You have {diff:.2f} leva left!")
else:
    print(f"Not enough money! You need {diff:.2f} leva more!")