#!/usr/bin/env python3

#Given a string of words, you need to find the highest scoring word.

#Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.

#You need to return the highest scoring word as a string.

#If two words score the same, return the word that appears earliest in the original string.

#All letters will be lowercase and all inputs will be valid.


# Functions:
def get_val(indx):
    return " abcdefghijklmnopqrstuvwxyz".index(indx)  # Returns 1 for "a" ... 26 for "z"
        
def high(words_string):
    # Split words into list
    words_list = words_string.split()
    max_score = 0
    max_score_word = ""
    for word in words_list:  # Iterate through all words in list
        score = 0
        for j in word:  # Iterate through all letters in word
            score = score + get_val(j)
#        print("DEBUG___ word= {} score= {}".format(word, score))
        if score > max_score:
            max_score = score
            max_score_word = word
#            print("DEBUG___ NEW max_word= {} max_score= {}".format(max_score_word, max_score))

#    print("DEBUG max_score_word= {} and max_score= {}".format(max_score_word, max_score))
    return max_score_word 

text1 = 'zttwlexviq xzswzwdwgi zyopozyde kwtoax sbbsskck aagktl ocpmnvuc vxrsom snnhjfsysv ypagnod brtpykvuux xdxuzyn hdgc zlbhowruo lilo ljfoae vlgh ofgqnorko otqvcyjsgl zezmrzpi aeoa ccs gzjkeneivw'  #  expected: 'xzswzwdwgi'
text2 = 'msp lsglnkut ofxezs dsd fqrglwh tjjamjvez' # expected: 'tjjamjvez'
text3 =  'mjm acbatf jedpeb snywjkj hexghj lyexrjuucg zprmjtmrsa tgeo znl' # expected: 'zprmjtmrsa'
text4 =  'vffhyv ebnux mivocjxbtg seahmrylfj kkuiv wcdiezajrz dtm tnwm dsa glojp fflb jdeeobmhqo kln rorv nimbbg nxxmdil wddrxy ruhobt okoebf'  # expected: 'mivocjxbtg'
text5 = "aa b"
text6 = "b aa"




def test_1():
    assert high('man i need a taxi up to ubud') == 'taxi'
def test_2():
    assert high('what time are we climbing up the volcano') == 'volcano'
def test_3():
    assert high('take me to semynak') == 'semynak'
def test_4():
    assert high('aa b') == 'aa'
def test_5():
    assert high('b aa') == 'b'
def test_6():
    assert high('bb d') == 'bb'
def test_7():
    assert high('d bb') == 'd'
def test_8():
    assert high("aaa b") == "aaa"
