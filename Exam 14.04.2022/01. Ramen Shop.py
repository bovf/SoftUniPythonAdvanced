from collections import deque


ramen_servings = [int(x) for x in input().split(", ")]
customers_list = deque([int(x) for x in input().split(", ")])

ramen = 0
customers = 0
while True:
    if len(ramen_servings) == 0 or len(customers_list) == 0:
        if ramen == 0 and len(ramen_servings) == 0:
            break
        if customers == 0 and len(customers_list) == 0:
            break
    if ramen < 1:
        ramen = ramen_servings.pop()
    if customers < 1:
        customers = customers_list.popleft()
    if ramen == customers:
        ramen = 0
        customers = 0
    elif ramen > customers:
        ramen -= customers
        customers = 0
    else:
        customers -= ramen
        ramen = 0

if ramen > 0:
    ramen_servings.append(ramen)

if customers > 0:
    customers_list.appendleft(customers)

if len(customers_list) == 0 and customers == 0:
    print("Great job! You served all the customers.")
    if len(ramen_servings) > 0:
        print(f"Bowls of ramen left: {', '.join([str(x) for x in ramen_servings])}")
else:
    print("Out of ramen! You didn't manage to serve all customers.")
    print(f"Customers left: {', '.join([str(x) for x in customers_list])}")
