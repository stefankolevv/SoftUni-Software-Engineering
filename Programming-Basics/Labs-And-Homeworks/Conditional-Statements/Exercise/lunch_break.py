import math

name_episode = input()
episode_duration = int(input())
break_duration = int(input())

lunch_time = break_duration / 8
relax_time = break_duration / 4

left_time = break_duration - lunch_time - relax_time

diff = abs(left_time - episode_duration)
rounded_diff = math.ceil(diff)
if left_time >= episode_duration:
    print(f"You have enough time to watch {name_episode} and left with {rounded_diff} minutes free time.")
else:
    print(f"You don't have enough time to watch {name_episode}, you need {rounded_diff} more minutes.")