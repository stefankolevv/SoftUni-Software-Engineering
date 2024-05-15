def clear_skies(n, *args):
    matrix = [list(row) for row in args]
    jetfighter_row, jetfighter_col = None, None
    jetfighter_armor = 300
    enemies_count = sum(row.count("E") for row in matrix)
    repair_points = sum(row.count("R") for row in matrix)

    for i in range(n):
        for j in range(n):
            if matrix[i][j] == "J":
                jetfighter_row, jetfighter_col = i, j

    while True:
        command = input()
        if command == "End":
            break

        new_row, new_col = jetfighter_row, jetfighter_col
        if command == "up":
            new_row -= 1
        elif command == "down":
            new_row += 1
        elif command == "left":
            new_col -= 1
        elif command == "right":
            new_col += 1

        if not (0 <= new_row < n and 0 <= new_col < n):
            continue

        if matrix[new_row][new_col] == "-":
            matrix[jetfighter_row][jetfighter_col] = "-"
            jetfighter_row, jetfighter_col = new_row, new_col
            matrix[jetfighter_row][jetfighter_col] = "J"
        elif matrix[new_row][new_col] == "E":
            enemies_count -= 1
            matrix[jetfighter_row][jetfighter_col] = "-"
            jetfighter_row, jetfighter_col = new_row, new_col
            matrix[jetfighter_row][jetfighter_col] = "J"
            if enemies_count == 0:
                return "Mission accomplished, you neutralized the aerial threat!\n" + "\n".join("".join(row) for row in matrix)
            jetfighter_armor -= 100
            if jetfighter_armor == 0:
                return f"Mission failed, your jetfighter was shot down! Last coordinates [{jetfighter_row}, {jetfighter_col}]!\n" + "\n".join("".join(row) for row in matrix)
        elif matrix[new_row][new_col] == "R":
            matrix[jetfighter_row][jetfighter_col] = "-"
            jetfighter_row, jetfighter_col = new_row, new_col
            matrix[jetfighter_row][jetfighter_col] = "J"
            jetfighter_armor = 300

    return "\n".join("".join(row) for row in matrix)


print(clear_skies(5,
                  "-R---",
                  "-J--E",
                  "-E---",
                  "--E-E",
                  "-R---"))

