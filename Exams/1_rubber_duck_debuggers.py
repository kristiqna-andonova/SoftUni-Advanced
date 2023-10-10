from collections import deque

programmers_time = deque([int(x) for x in input().split()])
tasks = [int(x) for x in input().split()]
duck_dict = {"Darth Vader Ducky": 0, "Thor Ducky": 0, "Big Blue Rubber Ducky": 0, "Small Yellow Rubber Ducky": 0}

while programmers_time and tasks:
    current_sum = programmers_time[0] * tasks[-1]

    if 0 <= current_sum <= 60:
        duck_dict["Darth Vader Ducky"] += 1
        programmers_time.popleft()
        tasks.pop()

    elif 61 <= current_sum <= 120:
        duck_dict["Thor Ducky"] += 1
        programmers_time.popleft()
        tasks.pop()

    elif 121 <= current_sum <= 180:
        duck_dict["Big Blue Rubber Ducky"] += 1
        programmers_time.popleft()
        tasks.pop()

    elif 122 <= current_sum <= 240:
        duck_dict["Small Yellow Rubber Ducky"] += 1
        programmers_time.popleft()
        tasks.pop()

    else:
        tasks[-1] -= 2
        programmers_time.rotate(-1)

print("Congratulations, all tasks have been completed! Rubber ducks rewarded:")
for key, value in duck_dict.items():
    print(f"{key}: {value}")


