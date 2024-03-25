import re

input_string = input()

regex = r'(\d{2})([-./])([A-Z][a-z]{2})\2(\d{4})'

matches = re.findall(regex, input_string)

for match in matches:
    day = match[0]
    month = match[2]
    year = match[3]
    print(f'Day: {day}, Month: {month}, Year: {year}')