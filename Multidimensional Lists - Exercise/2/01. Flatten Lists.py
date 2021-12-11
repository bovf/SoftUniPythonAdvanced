text = input()

matrix = []
first_list = text.split("|")
for lists in first_list:
    new = [x for x in lists.split(" ") if x != ""]
    matrix.append(new)
matrix.reverse()

for matrix_list in matrix:
    print(" ".join(matrix_list), end=" ")