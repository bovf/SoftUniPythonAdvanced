from collections import deque
import re


water_liters = int(input())
water_queue = deque([])
while True:
    command = input()
    if command == "Start":
        break
    else:
        water_queue.append(command)

pattern = r"refill+\s+(?P<liters>\d+)"
while True:
    command = input()
    if command == "End":
        print(f"{water_liters} liters left")
        break

    elif re.search(pattern, command):
        matches = re.finditer(pattern, command)
        refill_amount = 0
        for match in matches:
            refill_amount = int(match.group("liters"))
        water_liters += refill_amount

    else:
        if water_liters >= int(command):
            print(f"{water_queue.popleft()} got water")
            water_liters -= int(command)
        else:
            print(f"{water_queue.popleft()} must wait")
