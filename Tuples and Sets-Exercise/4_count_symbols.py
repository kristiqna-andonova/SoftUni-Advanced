text = sorted(tuple(input()))

dict_text = {}

for i in text:
    if i not in dict_text:
        dict_text[i] = text.count(i)
        print(f"{i}: {dict_text[i]} time/s")
