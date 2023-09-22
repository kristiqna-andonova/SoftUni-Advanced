rows = int(input())
matrix = [[char for char in list(input())] for row in range(rows)]

searched_element = input()
position = None

for row_index in range(rows):
    if position:
        break
    for col_index in range(len(matrix[row_index])):
        if matrix[row_index][col_index] == searched_element:
            print((row_index, col_index))
            position = (row_index, col_index)
            break
