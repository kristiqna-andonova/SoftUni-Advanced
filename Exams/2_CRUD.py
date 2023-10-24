rows, cols = 6, 6

matrix = [[el for el in input().split()] for r in range(rows)]

position = [int(x) for x in input()[1:-1].split(", ")]

possible_moves = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}

while True:
    command = input().split(", ")

    if command[0] == "Stop":
        break

    move = possible_moves[command[1]]
    row = position[0] + move[0]
    col = position[1] + move[1]
    position = [row, col]
    if command[0] == "Create":
        if matrix[row][col] == ".":
            matrix[row][col] = command[2]
            position = [row, col]
        else:
            continue

    elif command[0] == "Update":
        if matrix[row][col].isalnum():
            matrix[row][col] = command[2]
            position = [row, col]
        else:
            continue

    elif command[0] == "Delete":
        if matrix[row][col].isalnum():
            matrix[row][col] = "."
            position = [row, col]
        else:
            continue

    elif command[0] == "Read":
        if matrix[row][col].isalnum():
            position = [row, col]
            print(f"{matrix[row][col]}")
        else:
            continue

[print(*r, sep=" ") for r in matrix]

