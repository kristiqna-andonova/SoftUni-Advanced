rows = int(input())

matrix = []
mines = 0
ship = []
enemy = 0

for r in range(rows):
    matrix.append([el for el in input()])
    for c in range(rows):
        if matrix[r][c] == "S":
            ship = [r, c]

possible_moves = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}

while enemy < 3:
    if mines == 2:
        break

    command = input()
    move = possible_moves[command]
    row = ship[0] + move[0]
    col = ship[1] + move[1]
    if row < 0 or col < 0 or row >= rows or col >= rows:
        break
    if matrix[row][col] == "-":
        ship = [row, col]

    elif matrix[row][col] == "*":
        ship = [row, col]
        matrix[row][col] = "-"
        mines += 1

    elif matrix[row][col] == "C":
        ship = [row, col]
        matrix[row][col] = "-"
        enemy += 1

if not enemy:
    print("Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")
else:
    print(f"Mission failed, U-9 disappeared! Last known coordinates [{ship[0]}, {ship[1]}]!")

matrix[ship[0]][ship[1]] = "S"
[print(*x, sep="")for x in matrix]
