def team_lineup(*args):
    dict_c = {}
    result = ""
    for key in args:
        if key[1] not in dict_c:
            dict_c[key[1]] = []
        dict_c[key[1]].append(key[0])

    sorted_c = dict(sorted(dict_c.items(), key=lambda x: (-len(x[1]), x[0])))

    for k, value in sorted_c.items():
        result += f"{k}:\n"
        for player in value:
            result += f"  -{player}\n"

    return result.strip()


print(team_lineup(
   ("Harry Kane", "England"),
   ("Manuel Neuer", "Germany"),
   ("Raheem Sterling", "England"),
   ("Toni Kroos", "Germany"),
   ("Cristiano Ronaldo", "Portugal"),
   ("Thomas Muller", "Germany")))
