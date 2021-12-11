import sys
input_list = [int(x) for x in input().split(" ")]
number, length = input_list[0], input_list[1]
matrix = []
small_matrix_size = 3
for _ in range(number):
    matrix.append([int(x) for x in input().split(" ")])

max_sum = - sys.maxsize
for index_matrix in range(number - (small_matrix_size - 1)):
    for index_list in range(length - (small_matrix_size - 1)):
        sum_small_matrix = 0
        for small_row in range(index_matrix, index_matrix + small_matrix_size):
            col_sum = 0
            for small_col in range(index_list, index_list + small_matrix_size):
                current_num = matrix[small_row][small_col]
                col_sum += matrix[small_row][small_col]
            sum_small_matrix += col_sum
        if sum_small_matrix > max_sum:
            max_sum = sum_small_matrix
            index_row, index_col = small_row, small_col

# print(max_sum, top_left, top_right, bottom_left, bottom_right)
print(f"Sum = {max_sum}")
# print(index_row, index_col)

new_matrix = []
for new_matrix_row in range(index_row - (small_matrix_size - 1), index_row + 1):
    new_matrix_list = []
    for new_matrix_col in range(index_col - (small_matrix_size - 1), index_col + 1):
        new_matrix_list.append(str(matrix[new_matrix_row][new_matrix_col]))
    new_matrix.append(new_matrix_list)

for new_list in new_matrix:
    print(" ".join(new_list))