rows = int(input())
commands = input().split(", ")

matrix = []
squirrel = []

for row in range(rows):
    matrix.append([x for x in input()])
    for col in range(rows):
        if matrix[row][col] == "s":
            squirrel = [row, col]

possible_moves = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}
hazelnuts = 0
die = False
counter = 0

while counter < len(commands):
    for command in commands:
        move = possible_moves[command]
        row = squirrel[0] + move[0]
        col = squirrel[1] + move[1]

        if row < 0 or col < 0 or row >= rows or col >= rows:
            print("The squirrel is out of the field.")
            print(f"Hazelnuts collected: {hazelnuts}")
            die = True
            counter += 1
            quit()

        elif matrix[row][col] == "t":
            print("Unfortunately, the squirrel stepped on a trap...")
            print(f"Hazelnuts collected: {hazelnuts}")
            die = True
            counter += 1
            quit()

        elif matrix[row][col] == "h":
            hazelnuts += 1
            squirrel = [row, col]

        elif matrix[row][col] == "*":
            squirrel = [row, col]

        counter += 1

        if die:
            break

if hazelnuts == 3:
    print("Good job! You have collected all hazelnuts!")

if not die and hazelnuts < 3:
    print("There are more hazelnuts to collect.")

print(f"Hazelnuts collected: {hazelnuts}")
