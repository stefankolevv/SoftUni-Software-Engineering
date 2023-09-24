text = ["sand", "water", "fish", "sun"]

beach = input().lower()
count = sum(1 for word in text if word in beach)

print(count)
