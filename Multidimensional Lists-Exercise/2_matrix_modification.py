rows = int(input())
matrix = [[int(num) for num in input().split()] for row in range(rows)]

while True:
    command = input().split()

    if command[0] == "END":
        break
    r, c, v = [int(num) for num in command[1:]]
    if r < 0 or r >= rows or c < 0 or c >= rows:
        print("Invalid coordinates")

    if command[0] == "Add":
        matrix[r][c] += v

    if command[0] == "Subtract":
        matrix[r][c] -= v

for row in matrix:
    print(*row, sep=" ")