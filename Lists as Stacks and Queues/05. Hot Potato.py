from collections import deque

kids = input().split()
kids = deque(kids)
hot_number = int(input())

kid_number = 1
kid_index = 0
while len(kids) > 1:
    if kid_number == hot_number:
        print(f"Removed {kids[kid_index]}")
        del kids[kid_index]
        kid_number = 1
    else:
        kid_number += 1
        kid_index += 1
    if kid_index > len(kids) - 1:
        kid_index = 0
    else:
        pass
print(f"Last is {kids[0]}")
