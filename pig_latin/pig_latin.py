#!/usr/bin/env python3


#Simple Pig Latin

#Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.
#Examples

#pig_it('Pig latin is cool') # igPay atinlay siay oolcay
#pig_it('Hello world !')     # elloHay orldway !

# Tests:
def test_1():
    assert pig_it('Pig latin is cool') == "igPay atinlay siay oolcay"

def test_2():
    assert pig_it('Hello world !')     == "elloHay orldway !"


# Functions:
def rebuild_word(w):
    # If alphabetic, move first letter of word to end and add "ay"
    # Else leave as is
    if w.isalpha():
        new_word = w[1:] + w[:1] + "ay"
    return new_word

def rebuild_sentence(l):
    sentence = l[0]
    for j in range(1, len(l)):
        sentence += " " + l[j]
    return sentence
    
def pig_it(s):
    # Split sentence into words using spaces
    # Respell word
    # Create sentence with new words

    new_list = []
    word_list = s.split()
    for word in word_list:
        if word.isalpha(): 
            new_word = rebuild_word(word)
        else:
            new_word = word
        new_list.append(new_word)

        result = rebuild_sentence(new_list)
    return result
