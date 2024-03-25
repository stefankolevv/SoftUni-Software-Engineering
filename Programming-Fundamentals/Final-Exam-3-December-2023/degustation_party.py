def process_commands():
    liked_meals = {}
    unliked_count = 0

    while True:
        command = input()
        if command == "Stop":
            break

        tokens = command.split("-")
        action = tokens[0]
        guest = tokens[1]
        meal = tokens[2]

        if action == "Like":
            if guest not in liked_meals:
                liked_meals[guest] = []

            if meal not in liked_meals[guest]:
                liked_meals[guest].append(meal)
        elif action == "Dislike":
            if guest in liked_meals and meal in liked_meals[guest]:
                liked_meals[guest].remove(meal)
                print(f"{guest} doesn't like the {meal}.")
                unliked_count += 1
            elif guest not in liked_meals:
                print(f"{guest} is not at the party.")
            elif meal not in liked_meals[guest]:
                print(f"{guest} doesn't have the {meal} in his/her collection.")

    for guest, meals in liked_meals.items():
        print(f"{guest}: {', '.join(meals)}")

    print(f"Unliked meals: {unliked_count}")


if __name__ == "__main__":
    process_commands()
