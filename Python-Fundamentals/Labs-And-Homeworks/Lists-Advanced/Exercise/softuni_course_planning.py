schedule = input().split(", ")
commands = input()

while commands != "course start":
    command = commands.split(":")[0]
    lesson = commands.split(":")[1]

    if command == "Add":
        if lesson not in schedule:
            schedule.append(lesson)
    elif command == "Insert":
        index = int(commands.split(":")[2])
        if lesson not in schedule:
            schedule.insert(index, lesson)
    elif command == "Remove":
        if lesson in schedule:
            schedule.remove(lesson)
            if f"{lesson}-Exercise" in schedule:
                schedule.remove(f"{lesson}-Exercise")
    elif command == "Swap":
        second_lesson = commands.split(":")[2]
        if lesson in schedule and second_lesson in schedule:
            index1 = schedule.index(lesson)
            index2 = schedule.index(second_lesson)
            schedule[index1], schedule[index2] = schedule[index2], schedule[index1]
            if f"{lesson}-Exercise" in schedule and f"{second_lesson}-Exercise" not in schedule:
                exercise_index = schedule.index(f"{lesson}-Exercise")
                schedule.pop(exercise_index)
                index2 = schedule.index(second_lesson)
                schedule.insert(index2 + 1, f"{lesson}-Exercise")
            elif f"{second_lesson}-Exercise" in schedule and f"{lesson}-Exercise" not in schedule:
                exercise_index = schedule.index(f"{second_lesson}-Exercise")
                schedule.pop(exercise_index)
                index1 = schedule.index(lesson)
                schedule.insert(index1 + 1, f"{second_lesson}-Exercise")
    elif command == "Exercise":
        exercise = f"{lesson}-Exercise"
        if lesson in schedule and exercise not in schedule:
            lesson_index = schedule.index(lesson)
            schedule.insert(lesson_index + 1, exercise)

    commands = input()

for i in range(len(schedule)):
    print(f"{i+1}.{schedule[i]}")
