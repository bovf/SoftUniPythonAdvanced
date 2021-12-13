text = input()

matrix = []
first_list = text.split("|")
for lists in first_list:
    new = [x for x in lists.split(" ") if x != ""]
    matrix.append(new)
matrix.reverse()

new_list = []
for matrix_list in matrix:
    for list_element in matrix_list:
        new_list.append(list_element)

print(" ".join(new_list))
