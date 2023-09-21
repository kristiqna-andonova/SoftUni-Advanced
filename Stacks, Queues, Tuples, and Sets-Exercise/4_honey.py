import collections

bees = collections.deque([int(x) for x in input().split()])
nectar = [int(x) for x in input().split()]
process = collections.deque([x for x in input().split()])

honey = 0

while bees and nectar:
    if bees[0] >= nectar[-1]:
        nectar.pop()
    else:
        if nectar[-1] <= 0 and process[0] == "/":
            nectar.pop()
            bees.popleft()
            process.popleft()
        else:
            result = str(bees[0]) + str(process[0]) + str(nectar[-1])
            honey += abs(eval(result))
            bees.popleft()
            nectar.pop()
            process.popleft()

print(f"Total honey made: {honey}")
if bees:
    print(f"Bees left: {', '.join(str(x) for x in bees)}")

if nectar:
    print(f"Nectar left: {', '.join(str(x) for x in nectar)}")
