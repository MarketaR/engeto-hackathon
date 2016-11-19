#!/usr/bin/env python3

# define a function to load the dictionary to internal structure
# we will load it from external file
my_dict = []


def load_dict():
    with open("anagram_dict.txt", "r") as my_file:
        for line in my_file:
            my_dict.append(line.strip())
    return my_dict

load_dict()

# process the input word we're working with
input_word = input("Enter the word:")
input_list = list(sorted(input_word))
print(input_list)

for word in my_dict:
    sorted_word = list(sorted(word))
    result_word = []
    if sorted_word == input_list:
        result_word.append(word)
        print(result_word)
    else:
        pass


# def anagram_check(input_list):

# logic behind the anagram program
# ideal case - work with the internal structure (array) with all
# words from the dictionary and try to find proper letters in those words
# it is up to you how you'll handle this area, try to figure this out

# print the requested anagrams
