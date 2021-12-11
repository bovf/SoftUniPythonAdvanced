# + 96

r, c = tuple(int(x) for x in input().split())

matrix = []
for row in range(r):
    matrix_list = []
    letter_r = chr(row + 97)
    for col in range(c):
        letter_c = chr(col + row + 97)
        matrix_list.append(f"{letter_r}{letter_c}{letter_r}")
    matrix.append(matrix_list)
for row in matrix:
    for col in row:
        print(f"{col} ", end="")
    print("")