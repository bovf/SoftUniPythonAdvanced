number_of_intersections = int(input())
intersection_list = {}

for _ in range(number_of_intersections):
    intersection = input().split("-")
    first_cross_section = [int(x) for x in intersection[0].split(",")]
    second_cross_section = [int(x) for x in intersection[1].split(",")]
    intersection_start = max(first_cross_section[0], second_cross_section[0])
    intersection_end = min(first_cross_section[1], second_cross_section[1])

    numbers_in_intersection = []
    while intersection_start <= intersection_end:
        numbers_in_intersection.append(intersection_start)
        intersection_start += 1

    intersection_list[numbers_in_intersection] = len(numbers_in_intersection)

print(intersection_list)