num_resting_days = int(input())

working_days = 365 - num_resting_days
play_time_off_days = num_resting_days * 127
play_time_working_days = working_days * 63
total_play_time = play_time_off_days + play_time_working_days

if total_play_time > 30000:
    difference_minutes = total_play_time - 30000
    hours = difference_minutes // 60
    minutes = difference_minutes % 60
    print("Tom will run away")
    print(f"{hours} hours and {minutes} minutes more for play")
else:
    difference_minutes = 30000 - total_play_time
    hours = difference_minutes // 60
    minutes = difference_minutes % 60
    print("Tom sleeps well")
    print(f"{hours} hours and {minutes} minutes less for play")
