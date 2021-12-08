n = int(input())
matrix = []
for _ in range(n):
    matrix.append([x for x in input()])

wanted_symbol = ord(input())
is_it_found = False

for matrix_list in matrix:
    for symbol in matrix_list:
        if ord(symbol) == wanted_symbol:
            print(f"{matrix.index(matrix_list), matrix_list.index(symbol)}")
            is_it_found = True
            break
    if is_it_found:
        break

if not is_it_found:
    print(f"{chr(wanted_symbol)} does not occur in the matrix")
