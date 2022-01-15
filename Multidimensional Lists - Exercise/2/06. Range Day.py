matrix = []
for _ in range(5):
    matrix.append([x for x in input() if x != " "])

my_position = 0, 0

for row in range(len(matrix)):
    for col in range(len(matrix[row])):
        if matrix[row][col] == "A":
            my_position = row, col
n = int(input())
targets_hit = []

for _ in range(n):
    command = input().split()
    if command[0] == "move":
        matrix[my_position[0]][my_position[1]] = "."
        if command[1] == "left":
            if my_position[1] - int(command[2]) > -1 and matrix[my_position[0]][my_position[1] - int(command[2])] == ".":
                my_position = my_position[0], my_position[1] - int(command[2])
                if my_position[1] < 0:
                    my_position = my_position[0], 0
        elif command[1] == "right":
            if my_position[1] + int(command[2]) < 5 and matrix[my_position[0]][my_position[1] + int(command[2])] == ".":
                my_position = my_position[0], my_position[1] + int(command[2])
                if my_position[1] > 4:
                    my_position = my_position[0], 4
        elif command[1] == "up":
            if my_position[0] - int(command[2]) > -1 and matrix[my_position[0] - int(command[2])][my_position[1]] == ".":
                my_position = my_position[0] - int(command[2]), my_position[1]
                if my_position[0] < 0:
                    my_position = 0, my_position[1]
        elif command[1] == "down":
            if my_position[0] + int(command[2]) < 5 and matrix[my_position[0] + int(command[2])][my_position[1]] == ".":
                my_position = my_position[0] + int(command[2]), my_position[1]
                if my_position[0] > 4:
                    my_position = 4, my_position[1]
            matrix[my_position[0]][my_position[1]] = "A"
    if command[0] == "shoot":
        if command[1] == "left":
            for bullet in range(my_position[1], -1, -1):
                if matrix[my_position[0]][bullet] == "x":
                    target = [my_position[0], bullet]
                    targets_hit.append(target)
                    matrix[my_position[0]][bullet] = "."
                    break
        elif command[1] == "right":
            for bullet in range(my_position[1], 5):
                if matrix[my_position[0]][bullet] == "x":
                    target = [my_position[0], bullet]
                    targets_hit.append(target)
                    matrix[my_position[0]][bullet] = "."
                    break
        elif command[1] == "up":
            for bullet in range(my_position[0], -1, -1):
                if matrix[bullet][my_position[1]] == "x":
                    target = [bullet, my_position[1]]
                    targets_hit.append(target)
                    matrix[bullet][my_position[1]] = "."
                    break
        elif command[1] == "down":
            for bullet in range(my_position[0], 5):
                if matrix[bullet][my_position[1]] == "x":
                    target = [bullet, my_position[1]]
                    targets_hit.append(target)
                    matrix[bullet][my_position[1]] = "."
                    break

    number_targets = 0
    for row in matrix:
        for el in row:
            if el == "x":
                number_targets += 1
    if number_targets == 0:
        print(f"Training completed! All {len(targets_hit)} targets hit.")
        break
if number_targets != 0:
    print(f"Training not completed! {number_targets} targets left.")
for target in targets_hit:
    print(target)
