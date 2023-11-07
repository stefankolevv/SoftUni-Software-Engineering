contests = {}
users = {}

while True:
    command = input()
    if command == "no more time":
        break

    username, contest, points = command.split(" -> ")
    points = int(points)

    if contest not in contests:
        contests[contest] = []

    if username not in users:
        users[username] = {}

    if contest in users[username]:
        if points > users[username][contest]:
            users[username][contest] = points
    else:
        users[username][contest] = points
        contests[contest].append(username)

contests = dict(sorted(contests.items(), key=lambda x: x[0]))

for contest, participants in contests.items():
    participants.sort(key=lambda x: (-users[x][contest], x))

print("Contests:")
for contest, participants in contests.items():
    print(f"{contest}: {len(participants)} participants")
    for i, participant in enumerate(participants, start=1):
        points = users[participant][contest]
        print(f"{i}. {participant} <::> {points}")

users = dict(sorted(users.items(), key=lambda x: (-sum(x[1].values()), x[0])))

print("Individual standings:")
for i, (username, points) in enumerate(users.items(), start=1):
    total_points = sum(points.values())
    print(f"{i}. {username} -> {total_points}")
