def words_sorting(*args):
    word_list = list(args)
    words_sorted = {}
    result = ""
    total_sum = 0
    for word in word_list:
        ascii_val = 0
        for letter in word:
            ascii_val += ord(letter)
            words_sorted[word] = ascii_val
        total_sum += ascii_val

    if total_sum % 2 == 0:
        for typ in sorted(words_sorted.keys()):
            result += f"{typ} - {words_sorted[typ]}\n"
    else:
        for typ in sorted(words_sorted.keys(), key=lambda x: -words_sorted[x]):
            result += f"{typ} - {words_sorted[typ]}\n"

    return result


example = ('escape', 'charm', 'mythology')

example2 = (
        'escape',
        'charm',
        'eye')


print(words_sorting('escape', 'charm', 'mythology'))