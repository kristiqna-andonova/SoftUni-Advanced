from collections import deque
queue = deque()

peoples = input()

while peoples != "End":
    if peoples == "Paid":
        while queue:
            print(f"{queue.popleft()}")
    else:
        queue.append(peoples)

    peoples = input()

print(f"{len(queue)} people remaining.")