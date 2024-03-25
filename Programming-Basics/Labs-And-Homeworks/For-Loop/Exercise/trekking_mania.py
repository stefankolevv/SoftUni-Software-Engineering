num_of_groups = int(input())
total_num_of_climbers = 0
musala = 0
monblan = 0
kilimanjaro = 0
k2 = 0
everest = 0

for _ in range(num_of_groups):
    current_num_of_group = int(input())
    total_num_of_climbers += current_num_of_group

    if current_num_of_group <= 5:
        musala += current_num_of_group
    elif 6 <= current_num_of_group <= 12:
        monblan += current_num_of_group
    elif 13 <= current_num_of_group <= 25:
        kilimanjaro += current_num_of_group
    elif 26 <= current_num_of_group <= 40:
        k2 += current_num_of_group
    elif current_num_of_group > 40:
        everest += current_num_of_group

musala_percent = musala / total_num_of_climbers * 100
monblan_percent = monblan / total_num_of_climbers * 100
kilimanjaro_percent = kilimanjaro / total_num_of_climbers * 100
k2_percent = k2 / total_num_of_climbers * 100
everest_percent = everest / total_num_of_climbers * 100

print(f"{musala_percent:.2f}%")
print(f"{monblan_percent:.2f}%")
print(f"{kilimanjaro_percent:.2f}%")
print(f"{k2_percent:.2f}%")
print(f"{everest_percent:.2f}%")