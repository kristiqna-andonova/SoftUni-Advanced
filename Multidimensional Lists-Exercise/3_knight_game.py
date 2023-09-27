n = int(input())

matrix = []
knights = []

for row in range(n):
    matrix.append([x for x in input()])
    for col in range(n):
        if matrix[row][col] == 'K':
            knights.append([row, col])

removed_knights = 0
possible_moves = [(1, 2), (2, 1), (-1, 2), (1, -2), (-2, 1), (-1, -2), (-2, -1), (2, -1)]

while True:
    max_hits = 0
    max_knights = [0, 0]
    for k_row, k_col in knights:
        hits = 0
        for move in possible_moves:
            new_row = k_row + move[0]
            new_col = k_col + move[1]
            if 0 <= new_row < n and 0 <= new_col < n:
                if matrix[new_row][new_col] == 'K':
                    hits += 1

        if hits > max_hits:
            max_hits = hits
            max_knights = [k_row, k_col]

    if max_hits == 0:
        break
    knights.remove(max_knights)
    matrix[max_knights[0]][max_knights[1]] = "0"
    removed_knights += 1

print(removed_knights)