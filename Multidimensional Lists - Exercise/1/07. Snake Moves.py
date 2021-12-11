

def rotater(string, counter):
    if counter > (len(string) - 1):
        counter = 0
    letter = string[counter]
    counter += 1
    return counter, letter


rows, columns = tuple(int(x) for x in input().split())
matrix = []
for og_rows in range(rows):
    matrix_list = []
    for og_cols in range(columns):
        matrix_list.append(0)
    matrix.append(matrix_list)
count = 0
word = input()
for row in range(rows):
    if row % 2 == 0:
        for col in range(columns):
            count, letter = rotater(word, count)
            matrix[row][col] = letter

    else:
        for col in range(columns -1, -1, -1):
            count, letter = rotater(word, count)
            matrix[row][col] = letter

for row in matrix:
    for col in row:
        print(f"{col}", end="")
    print("")
