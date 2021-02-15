# Author: Tow Ms 2/12/21

def is_abecedarian(words, letters):
    with open("words.txt", "r") as infile:
        num_of_words = 0
        contents = infile.readlines()
        for words in contents:
            a = words.strip()
            b = sorted(a)
            if b == list(words):
                num_of_words += 1
            return num_of_words


print(is_abecedarian("a", "B"))