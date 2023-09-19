numbers = tuple(map(float, input().split()))
counter = {}

for num in numbers:
    if num not in counter:
        counter[num] = numbers.count(num)
        print(f"{num} - {counter[num]} times")
