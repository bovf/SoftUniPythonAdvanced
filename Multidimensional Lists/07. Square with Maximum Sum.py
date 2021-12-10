import sys
input_list = [int(x) for x in input().split(", ")]
number, length = input_list[0], input_list[1]
matrix = []

for _ in range(number):
    matrix.append([int(x) for x in input().split(", ")])

max_sum = - sys.maxsize
top_left, top_right, bottom_left, bottom_right = 0, 0, 0, 0
for index_matrix in range(number - 1):
    for index_list in range(length - 1):
        sum = matrix[index_matrix][index_list] + matrix[index_matrix + 1][index_list] + \
              matrix[index_matrix][index_list + 1] + matrix[index_matrix + 1][index_list + 1]
        if sum > max_sum:
            max_sum = sum
            top_left = index_matrix, index_list
            top_right = index_matrix, index_list + 1
            bottom_left = index_matrix + 1, index_list
            bottom_right = index_matrix + 1, index_list + 1
# print(max_sum, top_left, top_right, bottom_left, bottom_right)
print(f"{matrix[top_left[0]][top_left[1]]} {matrix[top_right[0]][top_right[1]]}")
print(f"{matrix[bottom_left[0]][bottom_left[1]]} {matrix[bottom_right[0]][bottom_right[1]]}")
print(max_sum)
