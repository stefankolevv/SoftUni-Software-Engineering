results = {}
languages = {}

while True:
    command = input()
    if command == "exam finished":
        break

    parts = command.split("-")
    if parts[-1] == "banned":
        username = parts[0]
        results.pop(username, None)
    else:
        username, language, points = parts
        points = int(points)

        if username not in results:
            results[username] = {}

        if language not in results[username]:
            results[username][language] = points
        else:
            results[username][language] = max(results[username][language], points)

        if language not in languages:
            languages[language] = 0
        languages[language] += 1

sorted_results = dict(sorted(results.items(), key=lambda x: (-max(x[1].values()), x[0])))

print("Results:")
for username, points in sorted_results.items():
    print(f"{username} | {max(points.values())}")

print("Submissions:")
for language, count in sorted(languages.items()):
    print(f"{language} - {count}")
