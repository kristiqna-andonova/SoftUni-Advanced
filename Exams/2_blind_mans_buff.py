rows, cols = [int(x) for x in input().split()]

matrix = []
blind_person = []
move_counter = 0
peoples = 0

for r in range(rows):
    matrix.append(input().split())
    for c in range(cols):
        if matrix[r][c] == "B":
            blind_person = [r, c]

possible_moves = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}

while True:
    command = input()

    if command == "Finish":
        break

    if peoples == 3:
        break

    move = possible_moves[command]
    row = blind_person[0] + move[0]
    col = blind_person[1] + move[1]

    if row < 0 or col < 0 or row >= rows or col >= cols:
        continue

    if matrix[row][col] == "-":
        blind_person = [row, col]
        move_counter += 1

    elif matrix[row][col] == "O":
        continue

    elif matrix[row][col] == "P":
        blind_person = [row, col]
        move_counter += 1
        peoples += 1

print("Game over!")
print(f"Touched opponents: {peoples} Moves made: {move_counter}")

