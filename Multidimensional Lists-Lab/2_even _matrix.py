r = int(input())
matrix = [[int(i) for i in input().split(", ")] for row in range(r)]

new_matrix = [[num for num in row if num % 2 == 0]for row in matrix]

print(new_matrix)
