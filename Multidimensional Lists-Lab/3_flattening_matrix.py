r = int(input())
matrix = [[int(num) for num in input().split(", ")]for row in range(r)]

flatten_matrix = [num for sublist in matrix for num in sublist]

print(flatten_matrix)