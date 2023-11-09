text = input().split()
new_text = [txt * len(txt) for txt in text]

print(''.join(new_text))
