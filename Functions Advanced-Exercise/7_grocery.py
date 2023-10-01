def grocery_store(**kwargs):
    recept = dict(sorted(kwargs.items(), key=lambda kvp: (-kvp[1], -len(kvp[0]), kvp[0])))
    result = []
    for product, quantity in recept.items():
        result.append(f'{product}: {quantity}')
    return "\n".join(result)


print(grocery_store(
    bread=5,
    pasta=12,
    eggs=12,
))
