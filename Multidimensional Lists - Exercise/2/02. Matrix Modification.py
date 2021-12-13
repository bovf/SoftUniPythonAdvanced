input_list = [int(x) for x in input().split(" ")]

number, length = input_list[0], input_list[0]
matrix = []
for _ in range(number):
    matrix.append([int(x) for x in input().split(" ")])

while True:
    command = input().split()
    if command[0] == "END":
        break
    row1, col1 = int(command[1]), int(command[2])
    if 0 <= row1 <= (number - 1) and 0 <= col1 <= (length - 1):
        if command[0] == "Add":
            matrix[row1][col1] += int(command[3])
        else:
            matrix[row1][col1] -= int(command[3])
    else:
        print("Invalid coordinates")
for row in matrix:
    for col in row:
        print(f"{col} ", end="")
    print("")
