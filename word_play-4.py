# Author: Tow Ms 2/12/21

def uses_only(word, letters):
    if letters.split().sort() == word.split().sort():
        return True


print(uses_only("racecar", "carraec"))

user_input = input("Input a string of letters\n")
a = user_input.split()
sorted(a)

with open("words.txt", "r") as infile:
    contents = infile.readlines()
    for value in contents:
        b = list(value.strip())
        c = sorted(b)
        if a == c:
            print(value)