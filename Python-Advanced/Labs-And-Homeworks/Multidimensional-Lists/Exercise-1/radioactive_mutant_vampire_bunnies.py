rows, cols = [int(item) for item in input().split()]
matrix = []

for _ in range(rows):
    matrix.append(list(input()))

commands = input()

# End of inputs


def find_player(matrix):
    stop = False
    postion = ()
    for r in range(rows):
        if stop:
            break
        for c in range(cols):
            if matrix[r][c] == 'P':
                postion = (r, c)
                stop = True
    return postion


def multiply_bunny(matrix, dead):
    bunnies_location = []
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            if matrix[r][c] == 'B':
                bunnies_location.append((r, c))

    for bun in bunnies_location:
        up = (bun[0] - 1, bun[1])
        down = (bun[0] + 1, bun[1])
        left = (bun[0], bun[1] - 1)
        right = (bun[0], bun[1] + 1)

        if 0 <= up[0] < rows and 0 <= up[1] < cols:
            if matrix[up[0]][up[1]] == 'P':
                dead = True
            matrix[up[0]][up[1]] = 'B'
        if 0 <= down[0] < rows and 0 <= down[1] < cols:
            if matrix[down[0]][down[1]] == 'P':
                dead = True
            matrix[down[0]][down[1]] = 'B'
        if 0 <= left[0] < rows and 0 <= left[1] < cols:
            if matrix[left[0]][left[1]] == 'P':
                dead = True
            matrix[left[0]][left[1]] = 'B'
        if 0 <= right[0] < rows and 0 <= right[1] < cols:
            if matrix[right[0]][right[1]] == 'P':
                dead = True
            matrix[right[0]][right[1]] = 'B'

    return dead, matrix


def move_player(loc, go, matrix, dead):
    out = False
    last = loc
    if go == 'U':
        new = (loc[0] - 1, loc[1])
        if 0 <= new[0] < rows and 0 <= new[1] < cols:
            last = new
            if matrix[new[0]][new[1]] == 'B':
                dead = True
                return last, dead, out, matrix
            else:
                matrix[new[0]][new[1]] = 'P'
                matrix[loc[0]][loc[1]] = '.'
                return last, dead, out, matrix
        else:
            out = True
            matrix[last[0]][last[1]] = '.'
            return last, dead, out, matrix

    elif go == 'D':
        new = (loc[0] + 1, loc[1])
        if 0 <= new[0] < rows and 0 <= new[1] < cols:
            last = new
            if matrix[new[0]][new[1]] == 'B':
                dead = True
                return last, dead, out, matrix
            else:
                matrix[new[0]][new[1]] = 'P'
                matrix[loc[0]][loc[1]] = '.'
                return last, dead, out, matrix
        else:
            out = True
            matrix[last[0]][last[1]] = '.'
            return last, dead, out, matrix

    elif go == 'L':
        new = (loc[0], loc[1] - 1)
        if 0 <= new[0] < rows and 0 <= new[1] < cols:
            last = new
            if matrix[new[0]][new[1]] == 'B':
                dead = True
                return last, dead, out, matrix
            else:
                matrix[new[0]][new[1]] = 'P'
                matrix[loc[0]][loc[1]] = '.'
                return last, dead, out, matrix
        else:
            out = True
            matrix[last[0]][last[1]] = '.'
            return last, dead, out, matrix

    elif go == 'R':
        new = (loc[0], loc[1] + 1)
        if 0 <= new[0] < rows and 0 <= new[1] < cols:
            last = new
            if matrix[new[0]][new[1]] == 'B':
                dead = True
                return last, dead, out, matrix
            else:
                matrix[new[0]][new[1]] = 'P'
                matrix[loc[0]][loc[1]] = '.'
                return last, dead, out, matrix
        else:
            out = True
            matrix[last[0]][last[1]] = '.'
            return last, dead, out, matrix

    return last, dead, out, matrix

# Main
dead = False
where = find_player(matrix)
for ch in commands:
    where, dead, out, matrix = move_player(where, ch, matrix, dead)
    dead, matrix = multiply_bunny(matrix, dead)
    if dead or out:
        break

if dead:
    for row in matrix:
        print(*row, sep="")

    print("dead: ", end='')
    print(*where, sep=' ')
else:
    for row in matrix:
        print(*row, sep="")
    print("won: ", end='')
    print(*where, sep=' ')
