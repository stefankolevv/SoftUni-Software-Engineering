name_serial = str(input())
num_seasons = int(input())
num_episodes = int(input())
time_per_episode = float(input())

duration_ads = time_per_episode * 0.2
duration_episode_with_ads = time_per_episode + duration_ads
bonus_time = num_seasons * 10
total_time = round(duration_episode_with_ads * num_episodes * num_seasons + bonus_time)

print(f"Total time needed to watch the {name_serial} series is {total_time} minutes.")
