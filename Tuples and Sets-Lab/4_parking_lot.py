lines = int(input())
parking = set()

for _ in range(lines):
    command = input().split(", ")
    if command[0] == "IN":
        parking.add(command[1])
    elif command[0] == "OUT":
        if command[1] in parking:
            parking.remove(command[1])

if parking:
    for car in parking:
        print(car)
else:
    print("Parking Lot is Empty")
