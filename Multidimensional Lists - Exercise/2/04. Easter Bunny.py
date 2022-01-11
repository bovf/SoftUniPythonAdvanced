n = int(input())
matrix = []
for _ in range(n):
    matrix.append([int(x) if x != "X" and x != "B" else x for x in input().split(" ")])

bunny_location = 0, 0
for row in range(len(matrix)):
    for col in range(len(matrix[row])):
        if matrix[row][col] == "B":
            bunny_location = row, col


def go_left(field, bunny):
    eggs_sum = 0
    bunny_x = bunny[1]
    bunny_y = bunny[0]
    steps = []
    while bunny_x > 0:
        bunny_x -= 1
        if field[bunny_y][bunny_x] == "X":
            return eggs_sum, steps
        steps.append([bunny_y, bunny_x])
        eggs_sum += field[bunny_y][bunny_x]
    return eggs_sum, steps


def go_right(field, bunny):
    eggs_sum = 0
    bunny_x = bunny[1]
    bunny_y = bunny[0]
    steps = []
    while bunny_x < len(field[bunny_y]) - 1:
        bunny_x += 1
        if field[bunny_y][bunny_x] == "X":
            return eggs_sum, steps
        steps.append([bunny_y, bunny_x])
        eggs_sum += field[bunny_y][bunny_x]
    return eggs_sum, steps


def go_up(field, bunny):
    eggs_sum = 0
    bunny_x = bunny[1]
    bunny_y = bunny[0]
    steps = []
    while bunny_y > 0:
        bunny_y -= 1
        if field[bunny_y][bunny_x] == "X":
            return eggs_sum, steps
        steps.append([bunny_y, bunny_x])
        eggs_sum += field[bunny_y][bunny_x]
    return eggs_sum, steps


def go_down(field, bunny):
    eggs_sum = 0
    bunny_x = bunny[1]
    bunny_y = bunny[0]
    steps = []
    while bunny_y < len(field) - 1:
        bunny_y += 1
        if field[bunny_y][bunny_x] == "X":
            return eggs_sum, steps
        steps.append([bunny_y, bunny_x])
        eggs_sum += field[bunny_y][bunny_x]
    return eggs_sum, steps


left_max, left_steps = go_left(matrix, bunny_location)
right_max, right_steps = go_right(matrix, bunny_location)
up_max, up_steps = go_up(matrix, bunny_location)
down_max, down_steps = go_down(matrix, bunny_location)

if up_max > right_max and up_max > left_max and up_max > down_max:
    print("up")
    for move in up_steps:
        print(move)
    print(up_max)

elif down_max > left_max and down_max > up_max and down_max > right_max:
    print("down")
    for move in down_steps:
        print(move)
    print(down_max)

elif left_max > right_max and left_max > up_max and left_max > down_max:
    print("left")
    for move in left_steps:
        print(move)
    print(left_max)

else:
    print("right")
    for move in right_steps:
        print(move)
    print(right_max)
