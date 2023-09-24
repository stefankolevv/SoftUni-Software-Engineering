time_pictures = int(input())
num_scenes = int(input())
time_scene = int(input())

field_preparation = time_pictures * 0.15
time_recording_scenes = num_scenes * time_scene
total_time = time_recording_scenes + field_preparation

if total_time <= time_pictures:
    rest_time = round(time_pictures - total_time)
    print(f"You managed to finish the movie on time! You have {rest_time} minutes left!")
else:
    needed_time = round(total_time - time_pictures)
    print(f"Time is up! To complete the movie you need {needed_time} minutes.")
