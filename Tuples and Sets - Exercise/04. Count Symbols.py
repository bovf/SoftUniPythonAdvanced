phrase = input()

characters = {}

for character in phrase:
    if character not in characters:
        characters[character] = 1
    else:
        characters[character] += 1

for character in sorted(characters.keys()):
    print(f"{character}: {characters[character]} time/s")
