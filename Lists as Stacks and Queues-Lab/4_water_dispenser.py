import collections

water = int(input())
queues = collections.deque()

names = input()

while names != "Start":
    queues.append(names)
    names = input()

liters = input().split()

while liters[0] != "End":
    if liters[0] == "refill":
        water += int(liters[1])
    elif len(liters) == 1:
        if int(liters[0]) <= water:
            person = queues.popleft()
            print(f"{person} got water")
            water -= int(liters[0])
        else:
            person = queues.popleft()
            print(f"{person} must wait")

    liters = input().split()

print(f"{water} liters left")
