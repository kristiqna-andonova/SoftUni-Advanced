from collections import deque

caffeine = [int(x) for x in input().split(", ")]
energy_drinks = deque([int(x) for x in input().split(", ")])

total_caffeine = 0

while caffeine and energy_drinks:
    current_sum = caffeine[-1] * energy_drinks[0]

    if current_sum + total_caffeine <= 300:
        total_caffeine += current_sum
        caffeine.pop()
        energy_drinks.popleft()

    else:
        caffeine.pop()
        energy_drinks.rotate(-1)
        if total_caffeine - 30 >= 0:
            total_caffeine -= 30

if energy_drinks:
    print(f"Drinks left: {', '.join([str(el) for el in energy_drinks])}")
else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")

print(f"Stamat is going to sleep with {total_caffeine} mg caffeine.")