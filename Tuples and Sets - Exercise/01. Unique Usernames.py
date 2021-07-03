usernames = set()

number_of_usernames = int(input())

for _ in range(number_of_usernames):
    username_input = input()
    usernames.add(username_input)

for name in usernames:
    print(name)
