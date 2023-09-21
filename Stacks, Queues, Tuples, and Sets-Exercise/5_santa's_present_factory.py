from collections import deque

materials = [int(x) for x in input().split()]
magic = deque([int(x) for x in input().split()])

toys = {150: "Doll", 250: "Wooden train", 300: "Teddy bear", 400: "Bicycle"}
toy_crafted = {}

while materials and magic:
    result = materials[-1] * magic[0]
    if result in toys:
        new_present = toys[result]
        if new_present not in toy_crafted:
            toy_crafted[new_present] = 0
        toy_crafted[new_present] += 1
        materials.pop()
        magic.popleft()

    elif result < 0:
        materials.append(materials.pop() + magic.popleft())

    elif result > 0:
        magic.popleft()
        materials[-1] += 15

    elif materials[-1] <= 0 and magic[0] <= 0:
        materials.pop()
        magic.popleft()

    elif materials[-1] <= 0:
        materials.pop()

    elif magic[0] <= 0:
        magic.popleft()


if ("Doll" in toy_crafted and "Wooden train" in toy_crafted) or ("Teddy bear" in toy_crafted
                                                                 and "Bicycle" in toy_crafted):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    print(f"Materials left: {', '.join(str(x) for x in materials[::-1])}")
if magic:
    print(f"Magic left: {', '.join(str(x) for x in magic)}")

for key, value in sorted(toy_crafted.items()):
    if value > 0:
        print(f"{key}: {value}")
