from collections import deque

text_lines = deque([int(x) for x in input().split()])
medicament = [int(x) for x in input().split()]

healing_items = {"Patch": 30, "Bandage": 40, "MedKit": 100}
items_h = {"Patch": 0, "Bandage": 0, "MedKit": 0}

while text_lines and medicament:
    last_medicament = medicament.pop()
    sum_items = text_lines.popleft() + last_medicament

    if sum_items > healing_items["MedKit"]:
        items_h["MedKit"] += 1
        medicament[-1] += sum_items - healing_items["MedKit"]

    elif sum_items == healing_items["Patch"]:
        items_h["Patch"] += 1

    elif sum_items == healing_items["Bandage"]:
        items_h["Bandage"] += 1

    elif sum_items == healing_items["MedKit"]:
        items_h["MedKit"] += 1
    else:
        last_medicament += 10
        medicament.append(last_medicament)

sorted_items = sorted(items_h.items(), key=lambda x: (-x[1], x[0]))

if not text_lines and not medicament:
    print("Textiles and medicaments are both empty.")
elif not text_lines:
    print("Textiles are empty.")
elif not medicament:
    print("Medicaments are empty.")

for item in sorted_items:
    if int(item[1]) > 0:
        print(f"{item[0]} - {item[1]}")

if medicament:
    medicament.reverse()
    print(f"Medicaments left: {', '.join(map(str, medicament))}")
if text_lines:
    print(f"Textiles left: {', '.join(map(str, text_lines))}")

