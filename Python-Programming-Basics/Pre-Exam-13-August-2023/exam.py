number_students = int(input())
grades = [float(input()) for _ in range(number_students)]

total_students = len(grades)
top_students = 0
between_4_and_4_99 = 0
between_3_and_3_99 = 0
failed_students = 0
average_grade = 0

for grade in grades:
    if grade >= 5.00:
        top_students += 1
    elif 4.00 <= grade <= 4.99:
        between_4_and_4_99 += 1
    elif 3.00 <= grade <= 3.99:
        between_3_and_3_99 += 1
    else:
        failed_students += 1

    average_grade += grade

average_grade /= total_students

print(f"Top students: {top_students / total_students * 100:.2f}%")
print(f"Between 4.00 and 4.99: {between_4_and_4_99 / total_students * 100:.2f}%")
print(f"Between 3.00 and 3.99: {between_3_and_3_99 / total_students * 100:.2f}%")
print(f"Fail: {failed_students / total_students * 100:.2f}%")
print(f"Average: {average_grade:.2f}")
