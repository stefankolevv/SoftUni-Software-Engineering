number_of_tournaments = int(input())
starting_points = int(input())

tournament_points = 0
number_of_wins = 0

for _ in range(number_of_tournaments):
    stage_of_the_tournament = input()

    if stage_of_the_tournament == "W":
        tournament_points += 2000
        number_of_wins += 1
    elif stage_of_the_tournament == "F":
        tournament_points += 1200
    elif stage_of_the_tournament == "SF":
        tournament_points += 720

total_points = starting_points + tournament_points
average_points_for_one_tournament = int(tournament_points / number_of_tournaments)
percent_of_wins = number_of_wins / number_of_tournaments * 100

print(f"Final points: {total_points}")
print(f"Average points: {average_points_for_one_tournament}")
print(f"{percent_of_wins:.2f}%")
