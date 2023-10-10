def tribonacci(n):
    tribonacci_sequence = [1, 1, 2]

    if n <= 3:
        return tribonacci_sequence[:n]

    for _ in range(3, n):
        next_tribonacci = sum(tribonacci_sequence[-3:])
        tribonacci_sequence.append(next_tribonacci)

    return tribonacci_sequence

n = int(input())
result = tribonacci(n)
print(" ".join(map(str, result)))
