rows = int(input())

matrix = []
ship = []
total_fish_count = 0
FISH_COUNT = 20

for r in range(rows):
    matrix.append([n for n in input()])
    for c in range(rows):
        if matrix[r][c] == "S":
            ship = [r, c]
            matrix[r][c] = "-"

possible_moves = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}

while True:
    command = input()

    if command == "collect the nets":
        break

    move = possible_moves[command]
    row = ship[0] + move[0]
    col = ship[1] + move[1]

    if row == rows:
        row = 0
        ship = [row, col]
    elif row == -1:
        row = rows - 1
        ship = [row, col]

    elif col == rows:
        col = 0
        ship = [row, col]
    elif col == -1:
        ship = [row, col]
        col = rows - 1

    if matrix[row][col].isnumeric():
        total_fish_count += int(matrix[row][col])
        matrix[row][col] = "-"
        ship = [row, col]

    elif matrix[row][col] == "W":
        ship = [row, col]
        print(f"You fell into a whirlpool! "
              f"The ship sank and you lost the fish you caught. Last coordinates of the ship: [{ship[0]},{ship[1]}"
              f"]")
        exit()

    ship = [row, col]

if total_fish_count >= FISH_COUNT:
    print("Success! You managed to reach the quota!")
elif 0 <= total_fish_count < FISH_COUNT:
    print(f"You didn't catch enough fish and didn't reach the quota! You need {abs(FISH_COUNT - total_fish_count)} tons of fish more.")

if total_fish_count > 0:
    print(f"Amount of fish caught: {total_fish_count} tons.")
matrix[ship[0]][ship[1]] = "S"
[print(*row_, sep="") for row_ in matrix]

