from collections import deque

monsters = deque([int(x) for x in input().split(",")])
soldiers = [int(x) for x in input().split(",")]

monster_count = 0

while True:
    if len(monsters) == 0:
        print("All monsters have been killed!")
        break
    elif len(soldiers) == 0:
        print("The soldier has been defeated.")
        break
    else:
        if monsters[0] <= soldiers[-1]:
            soldiers[-1] -= monsters[0]
            monsters.popleft()
            if soldiers:
                soldiers[-2] += soldiers[-1]
                soldiers.pop()
                monster_count += 1

        elif monsters[0] > soldiers[-1]:
            if monsters:
                monsters[0] -= soldiers[-1]
                soldiers.pop()
            monsters.rotate(-1)

print(f"Total monsters killed: {monster_count}")
