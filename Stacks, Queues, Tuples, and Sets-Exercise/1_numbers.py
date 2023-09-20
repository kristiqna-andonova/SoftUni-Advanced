first_set = set([int(x) for x in input().split()])
second_set = set([int(x) for x in input().split()])
line = int(input())

for _ in range(line):
    current_input = input().split()
    command = current_input[0] + " " + current_input[1]
    numbers = [int(x) for x in current_input[2:]]

    if command == "Add First":
        first_set.update(numbers)
    elif command == "Add Second":
        second_set.update(numbers)
    elif command == "Remove First":
        first_set.difference_update(numbers)
    elif command == "Remove Second":
        second_set.difference_update(numbers)
    elif command == "Check Subset":
        print(first_set.issubset(second_set) or second_set.issubset(first_set))

print(*sorted(first_set), sep=", ")
print(*sorted(second_set), sep=", ")
