n = int(input())

odd_set = set()
even_set = set()
for i in range(n):
    name = input()

    ascii_sum = 0
    for letter in name:
        ascii_sum += ord(letter)

    if (ascii_sum // (i + 1)) % 2 == 0:
        even_set.add(ascii_sum // (i + 1))
    else:
        odd_set.add(ascii_sum // (i + 1))

even_sum = sum(even_set)
odd_sum = sum(odd_set)


if even_sum == odd_sum:
    result = odd_set.union(even_set)
elif even_sum > odd_sum:
    result = odd_set.symmetric_difference(even_set)
else:
    result = odd_set.difference(even_set)

print(", ".join([str(x) for x in result]))
