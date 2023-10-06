with open("text.txt") as file:
    for row, line in enumerate(file.readlines()):
        if row % 2 == 0:
            for ch in ".,-!?":
                line = line.replace(ch, "@")
            print(" ".join(reversed(line.split())))
