expression = input()
stack = []

for i in range(len(expression)):
    if expression[i] == '(':
        stack.append(i)
    elif expression[i] == ')':
        start_i = stack.pop()
        print(expression[start_i:1+i])
