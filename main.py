def read_file_content(filename):
    # [assignment] Add your code here
    with open(filename) as f:
        lines = f.readlines()
        words = ""
        for line in lines:
            words = words+line
        return words


text = read_file_content("story.txt")

text = text.lower()
print(text)


def count_words():
    counts = dict()
    words = read_file_content("story.txt")
    words = words.split()
    for word in words:

        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts


word_dict = count_words()
print(word_dict)