# Author: Tow Ms 2/12/21

def is_abecedarian(words):
    lst = []
    for letters in words:
        lst.append(letters)
    if lst == sorted(words):
        return True
    else:
        return False


with open("words.txt", "r") as infile:
    num_of_words = 0
    contents = infile.readlines()
    for words in contents:
        lst2 = []
        alpha = words.strip()
        for lett in alpha:
            lst2.append(lett)
        if lst2 == sorted(alpha):
            num_of_words += 1 
print(num_of_words)


print(is_abecedarian("abc"))