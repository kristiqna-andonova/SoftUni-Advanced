r, c = [int(x) for x in input().split(", ")]

matrix = []
sum_matrix = 0

for row in range(r):
    line = [int(x) for x in input().split(", ")]
    matrix.append(line)
    sum_matrix += sum(line)

print(sum_matrix)
print(matrix)