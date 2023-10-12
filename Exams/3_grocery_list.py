def shop_from_grocery_list(budget, items_list, *args):
    for item, price in args:
        if item in items_list:
            if float(price) <= budget:
                items_list.remove(item)
                budget -= float(price)
            else:
                break
        continue

    if len(items_list) == 0:
        return f"Shopping is successful. Remaining budget: {budget:.2f}."
    else:
        return f"You did not buy all the products. Missing products: {', '.join([str(el) for el in items_list])}."


print(shop_from_grocery_list(
    100,
    ["tomato", "cola", "chips", "meat"],
    ("cola", 5.8),
    ("tomato", 10.0),
    ("meat", 22),
))
