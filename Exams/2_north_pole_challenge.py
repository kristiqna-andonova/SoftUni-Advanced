rows, cols = [int(x) for x in input().split(", ")]

you = []
matrix = []
cookies = 0
decorations = 0
gifts = 0
collect_all = False

for r in range(rows):
    matrix.append(input().split())
    for c in range(cols):
        if matrix[r][c] == "Y":
            you = [r, c]
            matrix[r][c] = "x"

command = input()
possible_moves = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}

while command != "End" and not collect_all:
    direction, steps = [x if x.isalpha() else int(x) for x in command.split("-")]

    for step in range(steps):
        move = possible_moves[direction]
        row = you[0] + move[0]
        col = you[1] + move[1]

        if row == rows:
            row = 0
            you = [row, col]
        elif row == -1:
            row = rows - 1
            you = [row, col]

        elif col == cols:
            col = 0
            you = [row, col]
        elif col == -1:
            you = [row, col]
            col = cols - 1

        if matrix[row][col] == "D":
            decorations += 1
        elif matrix[row][col] == "G":
            gifts += 1
        elif matrix[row][col] == "C":
            cookies += 1

        matrix[row][col] = "x"
        you = [row, col]

        if any([x != "." and x != "x" for row_ in matrix for x in row_]):
            continue
        else:
            collect_all = True
            break

    if not collect_all:
        command = input()

matrix[you[0]][you[1]] = "Y"
if collect_all:
    print("Merry Christmas!")
print("You've collected:")
print(f"- {decorations} Christmas decorations")
print(f"- {gifts} Gifts")
print(f"- {cookies} Cookies")
[print(*row) for row in matrix]