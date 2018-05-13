__author__ = 'Kalyan'

problem = """
Pig latin is an amusing game. The goal is to conceal the meaning of a sentence by a simple encryption.

Rules for converting a word to pig latin are as follows:

1. If word starts with a consonant, move all continuous consonants at the beginning to the end
   and add  "ay" at the end. e.g  happy becomes appyhay, trash becomes ashtray, dog becomes ogday etc.

2. If word starts with a vowel, you just add an ay. e.g. egg become eggay, eight becomes eightay etc.

You job is to write a program that takes a sentence from command line and convert that to pig latin and
print it back to console in a loop (till you hit Ctrl+C).

e.g "There is, however, no need for fear." should get converted to  "Erethay isay, oweverhay, onay eednay orfay earfay."
Note that punctuation and capitalization has to be preserved

You must write helper sub routines to make your code easy to read and write.

Constraints: only punctuation allowed is , and . and they will come immediately after a word and will be followed
by a space if there is a next word. Acronyms are not allowed in sentences. Some words may be capitalized
(first letter is capital like "There" in the above example) and you have to preserve its capitalization in the
final word too (Erethay)
"""

import sys
import re
def vowel_indx(wrd):
    vowels=['a','e','i','o','u']
    wrd=list(wrd)
    for i in wrd:
        if i in vowels:
            return wrd.index(i)


def pig_latin_encode(wrd):
    flag = 0
    if wrd.isalpha():
        if wrd[0].isupper():
            flag = 1
        wrd = wrd.lower()
        indx = vowel_indx(wrd)
        wrd = wrd[indx:]+wrd[0:indx]+"ay"
        if flag == 1:
            wrd = wrd.capitalize()
        return wrd
    else:
        return wrd

def pig_latin(source):
    result = []
    source=re.split('(\W)',source)
    for wrd in source:
        ret = pig_latin_encode(wrd)
        result.append(ret)
    result = "".join(result)
    return result



if __name__ == "__main__":
    source=sys.argv[1]
    result = pig_latin(source)
    print(result)