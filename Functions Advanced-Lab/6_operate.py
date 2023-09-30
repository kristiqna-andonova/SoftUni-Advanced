from functools import reduce


def operate(sing, *args):

    def add():
        return reduce(lambda a, b: a+b, args)

    def subtract():
        return reduce(lambda a, b: a-b, args)

    def divide():
        return reduce(lambda a, b: a/b, args)

    def multiply():
        return reduce(lambda a, b: a*b, args)

    if sing == "+":
        return add()
    elif sing == "-":
        return subtract()
    elif sing == "/":
        return divide()
    elif sing == "*":
        return multiply()


print(operate("+", 1, 2, 3))