word = input()
word_stack = list(word)


for _ in range(len(word_stack)):
    print(word_stack[-1], end="")
    word_stack.pop()
