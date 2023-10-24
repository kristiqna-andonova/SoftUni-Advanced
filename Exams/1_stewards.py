from collections import deque

seats = input().split(", ")
first_numbers = deque([int(x) for x in input().split(", ")])
second_numbers = [int(x) for x in input().split(", ")]

rotations = 0
seat = 0
matched_seats = []

while first_numbers and second_numbers or seat < 3 or rotations < 10:
    rotations += 1
    sum_num = first_numbers[0] + second_numbers[-1]
    found = False
    if str(first_numbers) + chr(sum_num) in seats:
        seat += 1
        first_numbers.popleft()
        second_numbers.pop()
        found = True
        matched_seats.append(f"{str(first_numbers)}{chr(sum_num)}")
    elif str(second_numbers) + chr(sum_num) in seats:
        seat += 1
        first_numbers.popleft()
        second_numbers.pop()
        found = True
        matched_seats.append(f"{str(second_numbers)}{chr(sum_num)}")
    else:
        first_numbers.rotate(-1)
        second_numbers.insert(0, second_numbers.pop())

    if found:
        continue

print(f"Seat matches: {', '.join(matched_seats)}")
print(f"Rotations count: {rotations}")