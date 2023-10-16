from collections import deque

food = [int(x) for x in input().split(", ")]
stamina = deque([int(x) for x in input().split(", ")])

mountains_dict = {"Vihren": 80, "Kutelo": 90, "Banski Suhodol": 100, "Polezhan": 60, "Kamenitza": 70}
peaks = []

while food and stamina and mountains_dict:
    sum_els = food.pop() + stamina.popleft()
    peak_name, difficult_level = list(mountains_dict.items())[0]

    if sum_els >= difficult_level:
        mountains_dict.pop(peak_name)
        peaks.append(peak_name)

if not mountains_dict:
    print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")

else:
    print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")

if peaks:
    print("Conquered peaks:")
    print(*peaks, sep="\n")
