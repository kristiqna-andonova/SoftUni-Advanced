lines = int(input())

table_set = set()

for _ in range(lines):
    element = input().split()
    for el in element:
        table_set.add(el)

print("\n".join(table_set))

