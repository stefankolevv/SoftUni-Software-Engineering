n = int(input())
students = {}

for _ in range(n):
    name = input()
    grade = float(input())

    if name not in students:
        students[name] = []
    students[name].append(grade)

filtered_students = {name: sum(grades) / len(grades) for name, grades in students.items() if
                     sum(grades) / len(grades) >= 4.5}

for name, average_grade in sorted(filtered_students.items(), key=lambda x: x[1], reverse=True):
    print(f"{name} -> {average_grade:.2f}")
