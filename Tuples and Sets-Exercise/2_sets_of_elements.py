ranges = input().split()

set_one = set()
set_two = set()

for _ in range(int(ranges[0])):
    set_one.add(int(input()))

for _ in range(int(ranges[1])):
    set_two.add(int(input()))

set_diff = set.intersection(set_one, set_two)

for n in set_diff:
    print(n)



