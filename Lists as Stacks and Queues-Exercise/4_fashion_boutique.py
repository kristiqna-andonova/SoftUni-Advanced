clothes = [int(x) for x in input().split()]
rack_capacity = int(input())
rack_count = 0

while clothes:
    rack_count += 1
    current_rack = rack_capacity
    while clothes and clothes[-1] <= current_rack:
        current_rack -= clothes.pop()

print(rack_count)