needed_experience = float(input())
count_of_battle = int(input())
experience_earned = float(input())

for num in range(count_of_battle):
    if count_of_battle == 3:
        experience_earned += 0.15 * experience_earned
    elif count_of_battle == 5:
        experience_earned -= 0.10 * experience_earned
    elif count_of_battle == 15:
        experience_earned += 0.5 * experience_earned
        total_experiece = sum(experience_earned)
        print(f"Player successfully collected his needed experience for {count_of_battle} battles.")

    else:
        needed_more_experience = diff(abs(total_experiece))
        print(f"Player was not able to collect the needed_experience, {needed_more_experience} more needed.")
