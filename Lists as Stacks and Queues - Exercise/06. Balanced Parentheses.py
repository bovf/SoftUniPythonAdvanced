from collections import deque

parentheses = list(input())
parentheses = deque(parentheses)
open_parentheses_123 = 0
open_parentheses = deque([])

while parentheses:
    left = parentheses.popleft()
    if left == "[":
        open_parentheses.append("[")
    elif left == "{":
        open_parentheses.append("{")
    elif left == "(":
        open_parentheses.append("(")
    elif left == ")":
        if open_parentheses:
            pass
        else:
            open_parentheses_123 -= 1
            break
        if open_parentheses.pop() == "(":
            pass
        else:
            open_parentheses_123 -= 1
            break

    elif left == "]":
        if open_parentheses:
            pass
        else:
            open_parentheses_123 -= 1
            break
        if open_parentheses.pop() == "[":
            pass
        else:
            open_parentheses_123 -= 1
            break

    elif left == "}":
        if open_parentheses:
            pass
        else:
            open_parentheses_123 -= 1
            break
        if open_parentheses.pop() == "{":
            pass
        else:
            open_parentheses_123 -= 1
            break


if len(parentheses) == 0 and open_parentheses_123 == 0:
    print("YES")
else:
    print("NO")
