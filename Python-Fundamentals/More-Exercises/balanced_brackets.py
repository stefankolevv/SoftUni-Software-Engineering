number = int(input())
stack = []

balanced = True

for _ in range(number):
    line = input()
    if line == "(":
        stack.append("(")
    elif line == ")":
        if stack:
            stack.pop()
        else:
            balanced = False
            break

if not stack and balanced:
    print("BALANCED")
else:
    print("UNBALANCED")
