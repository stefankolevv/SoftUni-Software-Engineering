import re

line = input()
pattern = r'\b[A-Z][a-z]+'

matches = re.findall(pattern, line)
sorted_matches = sorted(matches)

print(f"All extracted names: {', '.join(matches)}")
print(f"All extracted names (alphabetically sorted): {', '.join(sorted_matches)}")
print(f'Reversed text: {line[::-1]}')
