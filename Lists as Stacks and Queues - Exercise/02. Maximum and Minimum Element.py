number_count = int(input())

stack = []

for _ in range(number_count):
    command = input()

    if command.startswith("1"):
        stack.append(int(command.split()[-1]))
    elif command.startswith("2"):
        if len(stack) > 0:
            stack.pop()
        else:
            pass
    elif command.startswith("3"):
        if len(stack) > 0:
            print(max(stack))
        else:
            pass
    elif command.startswith("4"):
        if len(stack) > 0:
            print(min(stack))
        else:
            pass


while stack:
    if len(stack) > 1:
        print(stack.pop(), end=", ")
    else:
        print(stack.pop())
