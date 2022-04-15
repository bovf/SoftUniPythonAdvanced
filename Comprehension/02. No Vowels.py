text_To_convert = [x for x in input()]
vowels = ["a", "o", "e", "i", "u", "A", "O", "E", "I", "U"]
no_vowels = "".join([letter for letter in text_To_convert if letter not in vowels])
print(no_vowels)