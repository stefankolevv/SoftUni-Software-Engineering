import re

numbers = input()
valid_phone_numbers = []

regex = r'\+359-2-\d{3}-\d{4}\b|\+359 2 \d{3} \d{4}\b'
matches = re.findall(regex, numbers)

print(', '.join(matches))