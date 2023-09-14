import collections

kids = collections.deque(input().split())
turns = int(input()) - 1

while len(kids) != 1:
    kids.rotate(-turns)
    kid = kids.popleft()
    print(f"Removed {kid}")

last_kid = kids.popleft()
print(f"Last is {last_kid}")
