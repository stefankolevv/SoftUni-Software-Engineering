def read_matrix(size):
    matrix = []  # Empty maze matrix.
    for _ in range(size):
        matrix.append(list(input()))
    return matrix

def find_player(matrix):
    for y, row in enumerate(matrix):
        for x, char in enumerate(row):
            if char == 'P':
                return y, x

def move_player(y, x, command):
    # Commands to move the player - up, down, left and right.
    if command == 'up':
        return y - 1, x
    elif command == 'down':
        return y + 1, x
    elif command == 'left':
        return y, x - 1
    elif command == 'right':
        return y, x + 1

def is_inside(y, x, size):
    # Ensuring position validity within matrix boundaries.
    return 0 <= y < size and 0 <= x < size

n = int(input())
maze = read_matrix(n)
player_health = 100
player_y, player_x = find_player(maze)

while True:
    command = input()
    if not command:
        break

    next_y, next_x = move_player(player_y, player_x, command)
    if not is_inside(next_y, next_x, n):
        continue

    maze[player_y][player_x] = '-'

    if maze[next_y][next_x] == 'M':
        player_health -= 40
        if player_health <= 0:
            print('Player is dead. Maze over!')
            print(f"Player's health: 0 units")
            maze[next_y][next_x] = 'P'
            break
        else:
            maze[next_y][next_x] = 'P'

    elif maze[next_y][next_x] == 'H':
        player_health = min(100, player_health + 15)
        maze[next_y][next_x] = 'P'

    elif maze[next_y][next_x] == 'X':
        print('Player escaped the maze. Danger passed!')
        print(f"Player's health: {player_health} units")
        maze[next_y][next_x] = 'P'
        break

    elif maze[next_y][next_x] == '-':
        maze[next_y][next_x] = 'P'

    player_y, player_x = next_y, next_x

for row in maze:
    print(''.join(row))