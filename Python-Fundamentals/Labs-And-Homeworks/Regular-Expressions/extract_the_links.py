import re
 
pattern = r"(w{3}\.[A-Za-z0-9\-\.]+\.[a-z]+)"
line = input()
while line:
    match = re.search(pattern, line)
    if match:
        valid_url = match.group(1)
        print(valid_url)
    line = input()
