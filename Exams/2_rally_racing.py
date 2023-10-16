rows = int(input())
car_name = input()

matrix = []
tunnels = []
car = [0, 0]
kilometers = 0
finish = False

for r in range(rows):
    matrix.append(input().split())
    for c in range(rows):
        if matrix[r][c] == "T":
            tunnels.append((r, c))

possible_moves = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}

while True:
    command = input()

    if command == "End":
        break

    move = possible_moves[command]
    row = car[0] + move[0]
    col = car[1] + move[1]
    if row < 0 or col < 0 or row >= rows or col >= rows:
        break
    if (row, col) in tunnels:
        kilometers += 30
        matrix[row][col] = "."
        if (row, col) == tunnels[0]:
            car = tunnels[1]
            matrix[tunnels[1][0]][tunnels[1][1]] = "."
        else:
            matrix[tunnels[0][0]][tunnels[0][1]] = "."
            car = tunnels[0]

    elif matrix[row][col] == "F":
        kilometers += 10
        matrix[row][col] == "."
        car = [row, col]
        finish = True
        break

    else:
        car = [row, col]
        kilometers += 10

matrix[car[0]][car[1]] = "C"

if finish:
    print(f"Racing car {car_name} finished the stage!")
else:
    print(f"Racing car {car_name} DNF.")

print(f"Distance covered {kilometers} km.")
[print(''.join(x)) for x in matrix]
