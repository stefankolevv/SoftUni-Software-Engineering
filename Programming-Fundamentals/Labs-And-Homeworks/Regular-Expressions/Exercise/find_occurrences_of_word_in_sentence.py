import re

sentence = input()
searched_word = input()
pattern = fr"(?i)\b{searched_word}\b"
matches = re.findall(pattern, sentence)
print(len(matches))