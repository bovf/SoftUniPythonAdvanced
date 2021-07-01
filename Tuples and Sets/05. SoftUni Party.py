number_of_guests = int(input())

guest_keys = set()
for _ in range(number_of_guests):
    guest_passkey = input()
    guest_keys.add(guest_passkey)

while True:
    command = input()

    if command == "END":
        break
    else:
        guest_keys.remove(command)


print(len(guest_keys))
for guests_left in sorted(guest_keys):
    print(guests_left)
