rows, cols = [int(i) for i in input().split()]
matrix = [[str(char) for char in input().split()] for row in range(rows)]

max_sum = float("-inf")
max_row = 0
max_col = 0

for row in range(rows - 2):
    for col in range(cols - 2):
        sum_matrix = 0
        for r in range(row, row + 3):
            for c in range(col, col + 3):
                sum_matrix += int(matrix[r][c])
        if sum_matrix > max_sum:
            max_sum = sum_matrix
            max_row = row
            max_col = col

print(f"Sum = {max_sum}")
max_matrix = [matrix[r][max_col:max_col + 3] for r in range(max_row, max_row + 3)]
[print(*row) for row in max_matrix] 