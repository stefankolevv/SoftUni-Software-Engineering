def are_parentheses_balanced(expression):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}

    for char in expression:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping.keys():
            if not stack or stack.pop() != mapping[char]:
                return 'NO'
        else:
            continue

    return 'YES' if not stack else 'NO'

input_sequence = input()

result = are_parentheses_balanced(input_sequence)
print(result)