players = [{'name': x, 'rest': False} for x in input().split(", ")]
matrix = [input().split() for r in range(6)]

while True:
    player = players.pop(0)
    row, col = [int(x) for x in input()[1:-1].split(", ")]
    step = matrix[row][col]

    if player['rest']:
        player['rest'] = False

    elif step == "E":
        print(f"{player['name']} found the Exit and wins the game!")
        break

    elif step == "T":
        print(f"{player['name']} is out of the game! The winner is {players[0]['name']}.")
        break

    elif step == "W":
        player['rest'] = True
        print(f"{player['name']} hits a wall and needs to rest.")

    players.append(player) 