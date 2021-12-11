input_list = [int(x) for x in input().split(" ")]
number, length = input_list[0], input_list[1]
matrix = []
for _ in range(number):
    matrix.append([x for x in input().split(" ")])

while True:
    command = input().split()
    if command[0] == "END":
        break
    if not command[0] == "swap" or len(command) != 5:
        print("Invalid input!")
    else:
        row1, col1, row2, col2 = int(command[1]), int(command[2]), int(command[3]), int(command[4])
        if 0 <= row1 <= (number - 1) and 0 <= row2 <= (number - 1) and 0 <= col1 <= (length - 1) and\
                0 <= col2 <= (length - 1):
            matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
            for row in matrix:
                for col in row:
                    print(f"{col} ", end="")
                print("")
        else:
            print("Invalid input!")
