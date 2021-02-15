# Author: Tow Ms 2/12/21

def avoid(word, letters):
    if letters not in word:
        return True


print(avoid("hello", "g"))

user_input = input("What are the forbidden letters?\n")

with open("words.txt", "r") as infile:
    contents = infile.readlines()
    for value in contents:
        value_2 = str(value.strip())
        if user_input not in value_2:
            print(value_2)