number_of_commands = int(input())
cars_in_lot = set()

for _ in range(number_of_commands):
    command = input().split(", ")
    operation = command[0]
    license_number = command[1]
    if operation == "IN":
        cars_in_lot.add(license_number)
    else:
        cars_in_lot.remove(license_number)

if len(cars_in_lot) == 0:
    print("Parking Lot is Empty")
else:
    for car in cars_in_lot:
        print(car)
