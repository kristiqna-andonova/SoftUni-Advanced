def sorting_cheeses(**kwargs):
    sorted_cheeses = sorted(kwargs.items(), key=lambda kvp: (-len(kvp[1]), kvp[0]))
    result = ""
    for key, value in sorted_cheeses:
        result += f"{key}\n"
        sorted_values = sorted(value, reverse=True)
        result += "\n".join([str(el) for el in sorted_values])
        result += "\n"
    return result


print(
    sorting_cheeses(
        Parmesan=[102, 120, 135],
        Camembert=[100, 100, 105, 500, 430],
        Mozzarella=[50, 125],
    )
)
