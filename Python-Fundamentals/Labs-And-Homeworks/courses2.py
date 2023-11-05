courses = {}

while True:
    input_line = input()
    if input_line == "end":
        break

    course_name, student_name = input_line.split(" : ")

    if course_name not in courses:
        courses[course_name] = []

    courses[course_name].append(student_name)

sorted_courses = dict(sorted(courses.items(), key=lambda x: len(x[1]), reverse=True))

for course, students in sorted_courses.items():
    print(f"{course}: {len(students)}")
    for student in sorted(students):
        print(f"-- {student}")
