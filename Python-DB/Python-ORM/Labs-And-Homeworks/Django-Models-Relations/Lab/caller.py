import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Subject, Student, Lecturer, LecturerProfile

# Create queries within functions
# lecturer1 = Lecturer.objects.create(first_name="John", last_name="Doe")
#
# lecturer2 = Lecturer.objects.create(first_name="Jane", last_name="Smith")
#
# Subject.objects.create(name="Mathematics", code="MATH101", lecturer=lecturer1)
# Subject.objects.create(name="History", code="HIST101", lecturer=lecturer2)
# Subject.objects.create(name="Physics", code="PHYS101", lecturer=lecturer1)
# math_subject = Subject.objects.get(name="Mathematics")
# math_lecturer = math_subject.lecturer
# print(f"The lecturer for Mathematics is {math_lecturer}.")
# history_subject = Subject.objects.get(name="History")
# history_lecturer = history_subject.lecturer
# print(f"The lecturer for History is {history_lecturer}.")
# physics_subject = Subject.objects.get(name="Physics")
# physics_lecturer = physics_subject.lecturer
# print(f"The lecturer for Physics is {physics_lecturer}.")

# student1 = Student.objects.create(student_id="M1051", first_name="Alice",
# last_name="Johnson", birth_date="2000-01-15", email="a.johnson@abv.bg")
# student2 = Student.objects.create(student_id="S217", first_name="Bob",
# last_name="Smith", birth_date="2001-05-20", email="bobby@gmail.com")
# subject1 = Subject.objects.get(name="Mathematics")
# subject2 = Subject.objects.get(name="History")
# subject3 = Subject.objects.get(name="Physics")
# student1.subjects.add(subject1, subject2)
# student2.subjects.add(subject1, subject2, subject3)
#
# math_subject = Subject.objects.get(name="Mathematics")
# math_students = math_subject.student_set.all()
#
# for student in math_students:
#     print(f"{student.first_name} {student.last_name} is enrolled in Mathematics.")
#
# history_subject = Subject.objects.get(name="History")
# history_students = history_subject.student_set.all()
#
# for student in history_students:
#     print(f"{student.first_name} {student.last_name} is enrolled in History.")
#
# physics_subject = Subject.objects.get(name="Physics")
# physics_students = physics_subject.student_set.all()
#
# for student in physics_students:
#     print(f"{student.first_name} {student.last_name} is enrolled in Physics.")

# student = Student.objects.get(student_id="S217")
# student_enrollments = student.studentenrollment_set.all()
#
# for enrollment in student_enrollments:
#     print(f"{student.first_name} {student.last_name} is enrolled in {enrollment.subject}.")

# lecturer = Lecturer.objects.get(first_name='John', last_name="Doe")
# lecturer_profile = LecturerProfile.objects.create(lecturer=lecturer, email="john.doe@university.lecturers.com",
# bio="A skilled and passionate math lecturer", office_location="Sofia, Al. Stamobolyiski Str, Faculty of Mathematics and Computer Science, Room 101")
#
# lecturer_profile_from_db = LecturerProfile.objects.get(email='john.doe@university.lecturers.com')
#
# print(f"{lecturer_profile_from_db.lecturer.first_name} {lecturer_profile_from_db.lecturer.last_name} has a profile.")