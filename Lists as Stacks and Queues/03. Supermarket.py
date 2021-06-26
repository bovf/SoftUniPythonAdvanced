from collections import deque

queue = deque([])

while True:
    command = input()
    if command == "End":
        print(f"{len(queue)} people remaining.")
        break

    elif command == "Paid":
        while len(queue):
            print(f"{queue.popleft()}")
        queue = deque([])

    else:
        queue.append(command)
