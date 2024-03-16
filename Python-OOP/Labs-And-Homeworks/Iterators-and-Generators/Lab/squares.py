def squares(n):
    current = 1
    while current <= n:
        yield current ** 2
        current += 1

print(list(squares(5)))