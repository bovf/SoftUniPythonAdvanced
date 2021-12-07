matrix_size = [int(x) for x in input().split(", ")]
matrix = []
for _ in range(matrix_size[0]):
    matrix.append([int(x) for x in input().split(", ")])

result_sum = 0

for matrix_list in matrix:
    for num in matrix_list:
        result_sum += num

print(result_sum)
print(matrix)
