example_objects = {"Water Lilly": "flower",
                   "Swifts": "bird",
                   "Callery Pear": "tree",
                   "Swallows": "bird",
                   "Dahlia": "flower",
                   "Tulip": "flower",}

# print(start_spring(**example_objects))	flower:
#         -Dahlia
#         -Tulip
#         -Water Lilly
#         bird:
#         -Swallows
#         -Swifts
#         tree:
#         -Callery Pear



def start_spring(**kwargs):
    spring_flowers = {}
    result = ""
    for key, value in kwargs.items():
        if value not in spring_flowers.keys():
            spring_flowers[value] = [key]
        else:
            spring_flowers[value].append(key)

    for typ in sorted(spring_flowers.keys(), key=lambda x: (-len(spring_flowers[x]), x)):
        result += f"{typ}:\n"
        for obj in sorted(spring_flowers[typ]):
            result += f"-{obj}\n"

    return result


print(start_spring(**example_objects))
