import math

record_sec = float(input())
distance = float(input())
time_in_sec = float(input())

all_time_sec = distance * time_in_sec
delay = math.floor(distance / 15) * 12.5

total_time_plus_delay = all_time_sec + delay

if record_sec <= total_time_plus_delay:
    diff = total_time_plus_delay - record_sec
    print(f"No, he failed! He was {diff:.2f} seconds slower.")
else:
    print(f"Yes, he succeeded! The new world record is {total_time_plus_delay:.2f} seconds.")