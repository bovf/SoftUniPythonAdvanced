n = int(input())
matrix = []
for _ in range(n):
    matrix.append([x for x in input().split(", ")])

primary_diagonal = [int(matrix[x][x]) for x in range(len(matrix))]
secondary_diagonal = [int(matrix[x][(len(matrix) - 1) - x]) for x in range(len(matrix))]
# sum_diag = abs(sum(primary_diagonal) - sum(secondary_diagonal))
# print(sum_diag)
print(f"Primary diagonal: {', '.join([str(x) for x in primary_diagonal])}. Sum: {sum(primary_diagonal)}")
print(f"Secondary diagonal: {', '.join([str(x) for x in secondary_diagonal])}. Sum: {sum(secondary_diagonal)}")
