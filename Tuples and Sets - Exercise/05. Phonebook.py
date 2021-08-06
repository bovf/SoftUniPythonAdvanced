# noinspection PyBroadException
def iserror(func, *args, **kw):
    try:
        func(*args, **kw)
        return False
    except Exception:
        return True


address_book = {}
while True:
    command = input()
    if not iserror(int, command):
        break
    else:
        entry = command.split("-")
        address_book[entry[0]] = entry[1]


number_of_contacts = int(command)
for _ in range(number_of_contacts):
    name = input()
    if name not in address_book.keys():
        print(f"Contact {name} does not exist.")
    else:
        print(f"{name} -> {address_book[name]}")
