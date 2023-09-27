n = int(input())

matrix = []
bunnies = []

for row in range(n):
    matrix.append(input().split())
    for col in range(n):
        if matrix[row][col] == 'B':
            bunnies = [row, col]

possible_moves = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}
max_eggs = float("-inf")
max_directions = ""
max_move_matrix = []

for direction, moves in possible_moves.items():
    eggs = 0
    current_eggs = []
    row = bunnies[0] + moves[0]
    col = bunnies[1] + moves[1]

    while 0 <= row < n and 0 <= col < n:
        if matrix[row][col] == "X":
            break
        eggs += int(matrix[row][col])
        current_eggs.append([row, col])
        row += moves[0]
        col += moves[1]

    if eggs > max_eggs and current_eggs:
        max_eggs = eggs
        max_directions = direction
        max_move_matrix = current_eggs

print(max_directions)
[print(row) for row in max_move_matrix]
print(max_eggs)