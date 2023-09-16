import collections

quantity_food = int(input())
orders = collections.deque([int(x) for x in input().split()])

print(max(orders))

while orders and orders[0] <= quantity_food:
    quantity_food -= orders[0]
    orders.popleft()

if orders:
    print("Orders left:", end="")
    while orders:
        print(f" {orders.popleft()}", end="")
else:
    print("Orders complete")
