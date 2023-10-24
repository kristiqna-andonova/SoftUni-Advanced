from collections import deque

elfs = deque([int(n) for n in input().split()])
boxes = [int(n) for n in input().split()]

counter = 0
toys = 0
total_energy = 0

while boxes:
    while elfs[0] < 5:
        elfs.popleft()
        if len(elfs) == 0:
            break
    if len(elfs) == 0:
        break

    counter += 1

    if counter % 3 != 0:
        if elfs[0] >= boxes[-1]:
            if counter % 5 == 0:
                elfs[0] -= boxes[-1]
            else:
                elfs[0] -= boxes[-1] - 1
                toys += 1

            total_energy += boxes[-1]
            boxes.pop()
            elfs.rotate(-1)
        else:
            elfs[0] *= 2
            elfs.rotate(-1)

    elif counter % 3 == 0:
        if elfs[0] >= boxes[-1] * 2:
            if counter % 5 == 0:
                elfs[0] -= boxes[-1] * 2
            else:
                elfs[0] -= boxes[-1] * 2 - 1
                toys += 2

            total_energy += boxes[-1] * 2
            boxes.pop()
            elfs.rotate(-1)
        else:
            elfs[0] *= 2
            elfs.rotate(-1)

print(f"Toys: {toys}")
print(f"Energy: {total_energy}")

if len(elfs) > 0:
    print(f"Elves left: {', '.join([str(x) for x in elfs])}")
if len(boxes) > 0:
    print(f"Boxes left: {', '.join([str(x) for x in boxes])}")


