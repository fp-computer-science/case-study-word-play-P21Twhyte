# Author: Tow Ms 2/12/21

def word_check(word):
    if "e" not in word:
        return True


with open("words.txt") as old_file, open("words_without_e.txt", "w") as new_file:
    for line in old_file.readlines():
        if word_check(line):
            new_file.write(line)


with open("words.txt") as total_words, open("words_without_e.txt") as no_e_words:
    total_num = len(total_words.readlines())
    total_no_e = len(no_e_words.readline())
    percent = total_no_e/total_num * 100

print("{0} percent of the words didn't contain e".format(percent))