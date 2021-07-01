from collections import deque

max_quantity = int(input())

orders = [int(x) for x in input().split()]

orders = deque(orders)
print((max(orders)))
# orders.remove(orders[orders.index(max(orders))])

not_served = []
while orders:
    client = orders.popleft()
    if client > max_quantity:
        not_served.append(client)
        while orders:
            not_served.append(orders.popleft())
        break
    else:
        max_quantity -= client

if len(not_served) > 0:
    print(f"Orders left: {' '.join([str(x) for x in not_served])}")
else:
    print(f"Orders complete")
