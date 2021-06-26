clothes = [int(x) for x in input().split()]
rack_capacity = int(input())

sum = 0
hangers = 0
while clothes:
    clothe = clothes.pop()
    sum += clothe
    if sum > rack_capacity:
        clothes.append(clothe)
        sum = 0
        hangers += 1
    elif sum == rack_capacity:
        sum = 0
        hangers += 1
    else:
        pass
if sum > 0:
    hangers += 1
print(hangers)