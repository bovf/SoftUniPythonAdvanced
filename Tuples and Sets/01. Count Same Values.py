t = tuple(map(float, input().split()))
occurrences = {}

for num in t:
    if num not in occurrences:
        occurrences[num] = 0
    occurrences[num] += 1

for key in occurrences.keys():
    print(f"{key} - {occurrences[key]} times")
