# rows, cols = [int(x) for x in input().split()]
#
# matrix = []
# boy = []
# start_position = []
#
# for r in range(rows):
#     matrix.append([x for x in input()])
#     for c in range(cols):
#         if matrix[r][c] == "B":
#             boy = (r, c)
#             start_position = (r, c)
#
# possible_moves = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}
#
# while True:
#     command = input()
#     move = possible_moves[command]
#     row = boy[0] + move[0]
#     col = boy[1] + move[1]
#
#     if row < 0 or col < 0 or row >= rows or col >= cols:
#         print("The delivery is late. Order is canceled.")
#         matrix[start_position[0]][start_position[1]] = " "
#         break
#
#     if matrix[row][col] == "*":
#         continue
#
#     if matrix[row][col] == "-":
#         boy = [row, col]
#         matrix[row][col] = "."
#
#     if matrix[row][col] == "P":
#         matrix[row][col] = "R"
#         print("Pizza is collected. 10 minutes for delivery.")
#         boy = [row, col]
#
#     if matrix[row][col] == "A":
#         matrix[row][col] = "P"
#         boy = [row, col]
#         print("Pizza is delivered on time! Next order...")
#         break
#
# [print("".join(row)) for row in matrix]

rows, cols = [int(x) for x in input().split()]

matrix = []
boy = []
start = []

for row in range(rows):
    matrix.append([el for el in input()])
    for col in range(cols):
        if matrix[row][col] == "B":
            boy = [row, col]
            start = [row, col]

possible_moves = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}

while True:
    command = input()
    move = possible_moves[command]
    r = boy[0] + move[0]
    c = boy[1] + move[1]

    if 0 > r or 0 > c or r >= rows or c >= cols:
        print("The delivery is late. Order is canceled.")
        matrix[start[0]][start[1]] = " "
        break

    step_on = matrix[r][c]

    if step_on == "*":
        pass
    elif step_on == "P":
        boy = [r, c]
        matrix[r][c] = "R"
        print("Pizza is collected. 10 minutes for delivery.")
    elif step_on == "A":
        boy = [r, c]
        matrix[r][c] = "P"
        print("Pizza is delivered on time! Next order...")
        break
    elif step_on == "-":
        boy = [r, c]
        matrix[r][c] = "."

[print(*line, sep="") for line in matrix]
