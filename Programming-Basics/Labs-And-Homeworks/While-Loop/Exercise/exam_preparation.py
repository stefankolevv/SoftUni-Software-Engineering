number_poor_grades = int(input())

flag = False
count_poor = 0
sum_grades = 0
count_grades = 0
last_problem = ""
input_line = input()
while input_line != "Enough":
    current_grade = int(input())
    if current_grade <= 4:
        count_poor += 1

    if count_poor == number_poor_grades:
        flag = True
        break

    count_grades = count_grades + 1
    sum_grades = sum_grades + current_grade
    last_problem = input_line

    input_line = input()

if flag:
    print(f"You need a break, {count_poor} poor grades.")
else:
    avg_grade = sum_grades / count_grades
    print(f"Average score: {avg_grade:.2f}")
    print(f"Number of problems: {count_grades}")
    print(f"Last problem: {last_problem}")