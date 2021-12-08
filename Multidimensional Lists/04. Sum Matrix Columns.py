matrix_size = [int(x) for x in input().split(", ")]
matrix = []
for _ in range(matrix_size[0]):
    matrix.append([int(x) for x in input().split()])

for column in range(matrix_size[1]):
    sum_col = 0
    for row in range(matrix_size[0]):
        sum_col += matrix[row][column]
    print(sum_col)
