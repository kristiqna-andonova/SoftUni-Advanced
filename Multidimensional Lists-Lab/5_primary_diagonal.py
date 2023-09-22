n = int(input())
matrix = [[int(num) for num in input().split()] for row in range(n)]

sum_diagonal = 0
for r in range(n):
    sum_diagonal += matrix[r][r]

print(sum_diagonal)
