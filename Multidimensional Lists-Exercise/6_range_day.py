matrix = []
my_positions = []
targets = 0

for row in range(5):
    matrix.append(input().split())
    for col in range(5):
        if matrix[row][col] == "A":
            my_positions = [row, col]
        elif matrix[row][col] == "x":
            targets += 1

possible_moves = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}
targets_down = []
n = int(input())

for _ in range(n):
    command = input().split()

    if command[0] == "shoot":
        r = my_positions[0] + possible_moves[command[1]][0]
        c = my_positions[1] + possible_moves[command[1]][1]
        while 0 <= r < 5 and 0 <= c < 5:
            if matrix[r][c] == "x":
                matrix[r][c] = "."
                targets -= 1
                targets_down.append([r, c])
                break
            r += possible_moves[command[1]][0]
            c += possible_moves[command[1]][1]

        if targets == 0:
            print(f"Training completed! All {targets} targets hit.")
            break

    elif command[0] == "move":
        r = my_positions[0] + possible_moves[command[1]][0]
        c = my_positions[1] + possible_moves[command[1]][1]
        if 0 <= r < 5 and matrix[r][c] == ".":
            matrix[r][c] = "A"
            matrix[my_positions[0]][my_positions[1]] = "."
            my_positions = [r, c]

if targets > 0:
    print(f"Training not completed! {targets} targets left.")
[print(row) for row in targets_down]