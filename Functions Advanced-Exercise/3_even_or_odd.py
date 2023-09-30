def even_odd(*args):
    even = [x for x in args[:-1] if x % 2 == 0]
    odd = [x for x in args[:-1] if x % 2 != 0]

    command = args[-1]
    if command == 'odd':
        return odd
    elif command == 'even':
        return even


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
