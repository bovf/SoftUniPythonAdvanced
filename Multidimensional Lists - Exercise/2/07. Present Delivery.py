presents_number = int(input())
neighborhood = []
for _ in range(int(input())):
    neighborhood.append([x for x in input().split(" ")])

santa_position = 0, 0
for row in range(len(neighborhood)):
    for col in range(len(neighborhood[row])):
        if neighborhood[row][col] == "S":
            santa_position = row, col

nice_kids = 0
for row in neighborhood:
    for el in row:
        if el == "V":
            nice_kids += 1

santa_x, santa_y = santa_position[1], santa_position[0]
while presents_number > 0:
    # if neighborhood[santa_y - 1][santa_x] == "C":
    #     santa_x, santa_y = santa_x, santa_y - 1
    #     neighborhood[santa_y][santa_x] = "S"
    # if neighborhood[santa_y + 1][santa_x] == "C":
    #     santa_x, santa_y = santa_x, santa_y + 1
    #     neighborhood[santa_y][santa_x] = "S"
    # if neighborhood[santa_y][santa_x - 1] == "C":
    #     santa_x, santa_y = santa_x - 1, santa_y
    #     neighborhood[santa_y][santa_x] = "S"
    # if neighborhood[santa_y][santa_x + 1] == "C":
    #     santa_x, santa_y = santa_x + 1, santa_y
    #     neighborhood[santa_y][santa_x] = "S"
    command = input()

    if command == "up":
        neighborhood[santa_y][santa_x] = "-"
        santa_y -= 1
    elif command == "down":
        neighborhood[santa_y][santa_x] = "-"
        santa_y += 1
    elif command == "left":
        neighborhood[santa_y][santa_x] = "-"
        santa_x -= 1
    elif command == "right":
        neighborhood[santa_y][santa_x] = "-"
        santa_x += 1
    elif command == "Christmas morning":
        break
    if neighborhood[santa_y][santa_x] == "V":
        presents_number -= 1
        neighborhood[santa_y][santa_x] = "S"
    elif neighborhood[santa_y][santa_x] == "X":
        neighborhood[santa_y][santa_x] = "S"
    elif neighborhood[santa_y][santa_x] == "C":
        if neighborhood[santa_y - 1][santa_x] == "X" or neighborhood[santa_y - 1][santa_x] == "V":
            presents_number -= 1
            neighborhood[santa_y - 1][santa_x] = "-"
        if neighborhood[santa_y + 1][santa_x] == "X" or neighborhood[santa_y + 1][santa_x] == "V":
            presents_number -= 1
            neighborhood[santa_y + 1][santa_x] = "-"
        if neighborhood[santa_y][santa_x - 1] == "X" or neighborhood[santa_y][santa_x - 1] == "V":
            presents_number -= 1
            neighborhood[santa_y][santa_x - 1] = "-"
        if neighborhood[santa_y][santa_x + 1] == "X" or neighborhood[santa_y][santa_x + 1] == "V":
            presents_number -= 1
            neighborhood[santa_y][santa_x + 1] = "-"
        neighborhood[santa_y][santa_x] = "S"


nice_kids_left = 0
for row in neighborhood:
    for el in row:
        if el == "V":
            nice_kids_left += 1

if presents_number == 0 and nice_kids_left > 0:
    print("Santa ran out of presents!")

for row in neighborhood:
    print(" ".join(row))

if nice_kids_left == 0:
    print(f"Good job, Santa! {nice_kids} happy nice kid/s.")
else:
    print(f"No presents for {nice_kids_left} nice kid/s.")