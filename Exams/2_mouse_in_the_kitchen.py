rows, cols = [int(x) for x in input().split(",")]

matrix = []
cheeses = 0
mouse = []
final_position = []

for row in range(rows):
    matrix.append([x for x in input()])
    for col in range(cols):
        if matrix[row][col] == "M":
            mouse = (row, col)
            matrix[row][col] = "*"
        elif matrix[row][col] == "C":
            cheeses += 1

possible_moves = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}

while cheeses:
    command = input()

    if command == "danger":
        if cheeses:
            print("Mouse will come back later!")
            [print("".join(row)) for row in matrix]
            break
    move = possible_moves[command]
    row = mouse[0] + move[0]
    col = mouse[1] + move[1]

    if row < 0 or col < 0 or row >= rows or col >= cols:
        print("No more cheese for tonight!")
        matrix[final_position[0]][final_position[1]] = "M"
        [print("".join(row)) for row in matrix]
        break
    else:
        final_position = [row, col]

    if matrix[row][col] == "T":
        matrix[row][col] = "M"
        print("Mouse is trapped!")
        [print("".join(row)) for row in matrix]
        break

    if matrix[row][col] == "@":
        continue

    if matrix[row][col] == "C":
        mouse = [row, col]
        cheeses -= 1
        matrix[row][col] = "*"

    if matrix[row][col] == "*":
        mouse = [row, col]
        matrix[row][col] = "M"

    if matrix[row][col] == "M" and cheeses >= 1:
        matrix[row][col] = "*"

if cheeses == 0:
    print("Happy mouse! All the cheese is eaten, good night!")
    [print("".join(row)) for row in matrix]

