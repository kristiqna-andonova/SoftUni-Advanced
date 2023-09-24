rows = int(input())
matrix = [[int(num) for num in input().split(", ")] for row in range(rows)]

first_diagonal = 0
second_diagonal = 0
first_d = []
second_d = []

for row in range(rows):
    first_diagonal += matrix[row][row]
    first_d.append(matrix[row][row])
    second_diagonal += matrix[row][rows - row - 1]
    second_d.append(matrix[row][rows - row - 1])

print(f"Primary diagonal: {', '.join([str(i) for i in first_d])}. Sum: {first_diagonal}")
print(f"Secondary diagonal: {', '.join([str(i) for i in second_d])}. Sum: {second_diagonal}")
