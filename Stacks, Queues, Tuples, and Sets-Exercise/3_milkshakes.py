import collections

chocolates = [int(x) for x in input().split(", ")]
cups = collections.deque([int(x) for x in input().split(", ")])

milkshakes = 0

while chocolates and cups and milkshakes < 5:
    if chocolates[-1] <= 0 and cups[0] <= 0:
        chocolates.pop()
        cups.popleft()
        continue

    if chocolates[-1] <= 0:
        chocolates.pop()
        continue
    elif cups[0] <= 0:
        cups.popleft()
        continue
    if chocolates[-1] == cups[0]:
        milkshakes += 1
        chocolates.pop()
        cups.popleft()
    else:
        cups.rotate(-1)
        chocolates[-1] -= 5

if milkshakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")
print(f"Chocolate: {', '.join(str(x) for x in chocolates) if chocolates else 'empty'}")
print(f"Milk: {', '.join(str(x) for x in cups) if cups else 'empty'}")
