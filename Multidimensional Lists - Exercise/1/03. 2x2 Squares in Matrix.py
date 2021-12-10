n = int(input().split()[0])
matrix = []
for _ in range(n):
    matrix.append([x for x in input().split()])

squares = 0

for row in range(len(matrix) - 1):
    for column in range(len(matrix[row]) - 1):
        if matrix[row][column] == matrix[row + 1][column + 1] and matrix[row][column] == matrix[row][column + 1] and matrix[row][column] == matrix[row + 1][column]:
            squares += 1

print(squares)
