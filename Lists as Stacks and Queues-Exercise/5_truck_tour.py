from collections import deque

n = int(input())

pumps = deque()
start_position = 0
stops = 0

for i in range(n):
    fuel, distance = input().split()
    pumps.append([int(fuel), int(distance)])

while stops < n:
    fuel = 0
    for i in range(n):
        fuel += pumps[i][0]
        destination = pumps[i][1]
        if fuel < destination:
            pumps.rotate(-1)
            start_position += 1
            stops = 0
            break
        fuel -= destination
        stops += 1

print(start_position)
