row, col = [int(x) for x in input().split()]

start = ord("a")

for r in range(row):
    for c in range(col):
        print(f"{chr(start + r)}{chr(start + r + c)}{chr(start + r)}", end=" ")
    print()