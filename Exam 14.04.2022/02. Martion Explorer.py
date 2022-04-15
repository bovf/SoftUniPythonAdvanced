from collections import deque


def land_deposit(deposit_type, position: list):
    if deposit_type == "W":
        print(f"Water deposit found at ({position[0]}, {position[1]})")
    elif deposit_type == "M":
        print(f"Metal deposit found at ({position[0]}, {position[1]})")
    elif deposit_type == "C":
        print(f"Concrete deposit found at ({position[0]}, {position[1]})")


matrix = []
for _ in range(6):
    matrix.append(input().split())

rover_position = []
for row in range(6):
    for col in range(6):
        if matrix[row][col] == "E":
            rover_position = [row, col]


M, W, C = 0, 0, 0

commands = deque(input().split(", "))

while commands:
    command = commands.popleft()
    if command == "up":
        rover_position[0] = rover_position[0] - 1
        if rover_position[0] == -1:
            rover_position[0] = 5
    elif command == "down":
        rover_position[0] = rover_position[0] + 1
        if rover_position[0] == 6:
            rover_position[0] = 0
    elif command == "left":
        rover_position[1] = rover_position[1] - 1
        if rover_position[1] == -1:
            rover_position[1] = 5
    elif command == "right":
        rover_position[1] = rover_position[1] + 1
        if rover_position[1] == 6:
            rover_position[1] = 0

    block = matrix[rover_position[0]][rover_position[1]]
    if block == "W":
        land_deposit("W", rover_position)
        W = 1
    elif block == "M":
        land_deposit("M", rover_position)
        M = 1
    elif block == "C":
        land_deposit("C", rover_position)
        C = 1
    if block == "R":
        print(f"Rover got broken at ({rover_position[0]}, {rover_position[1]})")
        break

if W == 1 and M == 1 and C == 1:
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")
