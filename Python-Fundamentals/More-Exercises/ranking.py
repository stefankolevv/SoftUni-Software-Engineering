contests = {}
submissions = {}

while True:
    command = input()
    if command == "end of contests":
        break

    contest, password = command.split(":")
    contests[contest] = password

while True:
    submission = input()
    if submission == "end of submissions":
        break

    contest, password, username, points = submission.split("=>")
    points = int(points)

    if contest in contests and contests[contest] == password:
        if username not in submissions:
            submissions[username] = {}

        if contest not in submissions[username] or points > submissions[username][contest]:
            submissions[username][contest] = points

best_candidate = max(submissions, key=lambda x: sum(submissions[x].values()))

print(f"Best candidate is {best_candidate} with total {sum(submissions[best_candidate].values())} points.")
print("Ranking:")

for username in sorted(submissions.keys()):
    print(username)
    for contest, points in sorted(submissions[username].items(), key=lambda x: -x[1]):
        print(f"#  {contest} -> {points}")
