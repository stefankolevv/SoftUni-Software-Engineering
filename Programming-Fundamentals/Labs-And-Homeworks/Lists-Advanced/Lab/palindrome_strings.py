strings = input().split()
searched_palindrome = input()
palindromes = []

for word in strings:
    if word == "".join(reversed(word)):
        palindromes.append(word)

print(f"{palindromes}")
print(f"Found palindrome {palindromes.count(searched_palindrome)} times")