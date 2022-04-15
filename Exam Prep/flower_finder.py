from collections import deque

flowers = ["rose", "tulip", "lotus", "daffodil"]
flowers_modified = ["rose", "tulip", "lotus", "daffodil"]

vowels = deque(input().split(" "))
consonants = input().split(" ")
flower_index = -1
while vowels and consonants:
    vowel = vowels.popleft()
    consonant = consonants.pop()

    for plant_index in range(len(flowers_modified)):
        if vowel in flowers_modified[plant_index]:
            flowers_modified[plant_index] = flowers_modified[plant_index].replace(vowel, "")
        if consonant in flowers_modified[plant_index]:
            flowers_modified[plant_index] = flowers_modified[plant_index].replace(consonant, "")

    if "" in flowers_modified:
        flower_index = flowers_modified.index("")
        break


if flower_index != -1:
    print(f"Word found: {flowers[flower_index]}")
else:
    print(f"Cannot find any word!")

if vowels:
    print(f"Vowels left: {' '.join(vowels)}")
if consonants:
    print(f"Consonants left: {' '.join(consonants)}")
