rows, cols = [int(num) for num in input().split(", ")]
matrix = [[int(num) for num in input().split(", ")]for row in range(rows)]
max_sum = float("-inf")
max_sub_matrix = []

for row in range(rows - 1):
    for col in range(cols - 1):
        current_element = matrix[row][col]
        next_element = matrix[row][col + 1]
        element_below = matrix[row + 1][col]
        element_right = matrix[row + 1][col + 1]
        sum_element = current_element + next_element + element_right + element_below

        if sum_element >= max_sum:
            max_sum = sum_element
            max_sub_matrix = [[current_element, next_element], [element_below, element_right]]

print(*max_sub_matrix[0])
print(*max_sub_matrix[1])
print(max_sum)
