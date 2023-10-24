from collections import deque

fuel = [int(x) for x in input().split()]
consumption = deque([int(x) for x in input().split()])
needed_fuel = deque([int(x) for x in input().split()])

counter = 0
is_moving = True
altitude = []
is_done = False

while is_moving:
    if not is_moving:
        break

    if not needed_fuel:
        is_done = True
        break

    subtract = fuel[-1] - consumption[0]

    if subtract >= needed_fuel[0]:
        counter += 1
        print(f"John has reached: Altitude {counter}")
        altitude.append(f"Altitude {counter}")
        fuel.pop()
        consumption.popleft()
        needed_fuel.popleft()
    else:
        counter += 1
        print(f"John did not reach: Altitude {counter}")
        if subtract < needed_fuel[0] and altitude:
            print("John failed to reach the top.")
            print(f"Reached altitudes: {', '.join([str(el) for el in altitude])}")
        elif subtract < needed_fuel[0] and len(altitude) == 0:
            print("John failed to reach the top.\nJohn didn't reach any altitude.")
        is_moving = False

if is_done:
    print("John has reached all the altitudes and managed to reach the top!")


# if not fuel and not altitude and not is_done:
#     print("John failed to reach the top.\nJohn didn't reach any altitude.")
# elif not needed_fuel and is_done:
#     print("John has reached all the altitudes and managed to reach the top!")
# elif not fuel and altitude or not is_done:
#     print("John failed to reach the top.")
#     print(f"Reached altitudes: {', '.join([str(el) for el in altitude])}")