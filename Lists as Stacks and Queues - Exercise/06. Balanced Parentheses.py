from collections import deque

parentheses = list(input())
parentheses = deque(parentheses)
open_parentheses_40 = 0
open_parentheses_91 = 0
open_parentheses_123 = 0
closed_parentheses_41 = 0

while parentheses:
    left = ord(parentheses.popleft())
    if left == 40:
        if right == 41:
            pass
        else:
            break
    elif left == 91:
        if right == 93:
            pass
        else:
            break
    elif left == 123:
        if right == 125:
            pass
        else:
            break
    else:
        break

if len(parentheses) == 0:
    print("YES")
else:
    print("NO")
