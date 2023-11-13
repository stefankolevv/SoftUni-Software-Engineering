import re

def extract_person_info(text):
    name_pattern = r'@([A-Za-z]+)\|'
    age_pattern = r'#(\d+)\*'

    names = re.findall(name_pattern, text)
    ages = re.findall(age_pattern, text)

    for name, age in zip(names, ages):
        print(f"{name} is {age} years old.")

n = int(input())

for _ in range(n):
    line = input()
    extract_person_info(line)
