n = int(input())
matrix = []
for _ in range(n):
    matrix.append([int(x) for x in input().split(", ")])

result = []
for matrix_list in matrix:
    result += matrix_list

print(result)
