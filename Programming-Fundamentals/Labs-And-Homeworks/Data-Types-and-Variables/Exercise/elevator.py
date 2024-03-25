from math import ceil

persons = int(input())
capacity = int(input())
courses = ceil(persons / capacity)

print(courses)