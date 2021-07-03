lengths = [int(x) for x in input().split()]

length_of_first_set = lengths[0]
length_of_second_set = lengths[1]

first_set = set()
second_set = set()

for _ in range(length_of_first_set + length_of_second_set):
    number = int(input())
    if len(first_set) < length_of_first_set:
        first_set.add(number)
    else:
        second_set.add(number)


def smaller_set(set_one, set_two):
    if len(set_one) <= len(set_two):
        return set_one, set_two
    else:
        return set_two, set_one


repeating_elements = []

for number in first_set:
    if number not in second_set:
        pass
    else:
        repeating_elements.append(number)


# for number in smaller_set(first_set, second_set)[0]:
#     if number not in smaller_set(first_set, second_set)[1]:
#         pass
#     else:
#         repeating_elements.append(number)

for element in repeating_elements:
    print(element)
