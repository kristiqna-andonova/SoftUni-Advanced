n = int(input())

matrix = []
alice = []

for row in range(n):
    matrix.append(input().split())
    for col in range(n):
        if matrix[row][col] == 'A':
            alice = [row, col]
            matrix[row][col] = "*"

possible_moves = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}
bags = 0

while bags < 10:
    command = input()
    move = possible_moves[command]
    row = alice[0] + move[0]
    col = alice[1] + move[1]

    if row < 0 or col < 0 or row >= n or col >= n:
        break

    if matrix[row][col] == 'R':
        matrix[row][col] = "*"
        break

    if matrix[row][col] not in "*.":
        bags += int(matrix[row][col])
    matrix[row][col] = "*"
    alice = [row, col]

if bags >= 10:
    print("She did it! She went to the party.")
else:
    print("Alice didn't make it to the tea party.")

[print(" ".join(row)) for row in matrix]
