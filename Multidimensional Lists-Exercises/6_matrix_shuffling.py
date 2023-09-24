def is_valid(r1, c1, r2, c2, row, col):
    return 0 <= r1 < row and 0 <= c1 < col and 0 <= r2 < row and 0 <= c2 < col


r, c = [int(x) for x in input().split()]
matrix = [[int(num) for num in input().split()] for row in range(r)]

while True:
    line = input()

    if line == "END":
        break

    command = line.split()
    if command[0] != "swap" or len(command) != 5:
        print("Invalid input!")
        continue

    row1, col1, row2, col2 = [int(num) for num in command[1:]]

    if is_valid(row1, col1, row2, col2, r, c):
        matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
        [print(*row) for row in matrix]
    else:
        print("Invalid input!")

