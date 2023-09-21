rows, cols = [int(num)for num in input().split(",")]
matrix = [[int(num) for num in input().split()] for row in range(rows)]

result = []

for col in range(cols):
    col_sum = 0
    for r in range(rows):
        col_sum += matrix[r][col]
    result.append(col_sum)

[print(x) for x in result]
