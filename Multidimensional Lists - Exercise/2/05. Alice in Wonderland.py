n = int(input())
matrix = []

for _ in range(n):
    matrix.append([x for x in input().split(" ")])

alice_location = 0, 0
for row in range(len(matrix)):
    for col in range(len(matrix[row])):
        if matrix[row][col] == "A":
            alice_location = row, col

total_tea = 0
tea_collected = False
alice_location_y = alice_location[0]
alice_location_x = alice_location[1]
matrix[alice_location_y][alice_location_x] = "*"
while True:
    direction = input()
    if direction == "right":
        alice_location_x += 1
    elif direction == "left":
        alice_location_x -= 1
    elif direction == "up":
        alice_location_y -= 1
    elif direction == "down":
        alice_location_y += 1
    if alice_location_x < 0:
        break
    if alice_location_y < 0:
        break
    if alice_location_y > len(matrix) - 1:
        break
    if alice_location_x > len(matrix) - 1:
        break
    try:
        total_tea += int(matrix[alice_location_y][alice_location_x])
    except:
        pass
    if matrix[alice_location_y][alice_location_x] == "R":
        matrix[alice_location_y][alice_location_x] = "*"
        break
    matrix[alice_location_y][alice_location_x] = "*"
    if total_tea >= 10:
        tea_collected = True
        break

if tea_collected:
    print("She did it! She went to the party.")
else:
    print("Alice didn't make it to the tea party.")

for row in matrix:
    print(" ".join(row))
