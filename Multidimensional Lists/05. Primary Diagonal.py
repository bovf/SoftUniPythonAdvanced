n = int(input())
matrix = []
for _ in range(n):
    matrix.append([int(x) for x in input().split()])

sum_diag = 0
for i in range(len(matrix)):
    sum_diag += matrix[i][i]

print(sum_diag)
