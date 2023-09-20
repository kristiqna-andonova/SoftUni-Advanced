import math
from collections import deque

expression = input().split()
numbers = deque()

for char in expression:
    if char not in "+-*/":
        numbers.append(int(char))
    else:
        while len(numbers) > 1:
            first_num = numbers.popleft()
            second_num = numbers.popleft()
            result = str(first_num) + char + str(second_num)
            numbers.appendleft(math.floor(eval(result)))

print(numbers[-1])
