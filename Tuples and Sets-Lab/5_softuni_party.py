lines = int(input())
guest_list = set()

for _ in range(lines):
    guest_list.add(input())

while True:
    command = input()

    if command == "END":
        print(len(guest_list))
        for guest in sorted(guest_list):
            print(guest)
        break

    else:
        if command in guest_list:
            guest_list.remove(command)
