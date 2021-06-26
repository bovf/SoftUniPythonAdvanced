from collections import deque

pumps_number = int(input())

pumps = []

for _ in range(pumps_number):
    pump = [int(x) for x in input().split()]
    pumps.append(pump)

pumps = deque(pumps)


rotation_success = False
pump_index = 0
for rotation in range(len(pumps) + 1):
    tank = 0
    fuel = 0
    distance = 0
    pump_stations = deque(pumps)
    pumps_completed = 0
    while pump_stations:
        pump_station = pump_stations.popleft()
        fuel = pump_station[0]
        distance = pump_station[1]
        tank += fuel
        if tank < distance:
            break
        else:
            tank -= distance
        pumps_completed += 1

    if pumps_completed == (len(pumps)):
        rotation_success = True
        break
    pumps.rotate(-1)
    pump_index += 1

if rotation_success:
    print(pump_index)
