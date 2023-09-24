rows = int(input())
matrix = [[int(num) for num in input().split()] for row in range(rows)]

first_diagonal = 0
second_diagonal = 0

for row in range(rows):
    first_diagonal += matrix[row][row]
    second_diagonal += matrix[row][rows - row - 1]

difference = abs(first_diagonal - second_diagonal)

print(difference)
