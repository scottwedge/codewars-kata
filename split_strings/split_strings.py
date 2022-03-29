#!/usr/bin/env python3

#Complete the solution so that it splits the string into pairs of two characters. If the string contains an odd number of characters then it should replace the missing second character of the final pair with an underscore ('_').

#Examples:

#* 'abc' =>  ['ab', 'c_']
#* 'abcdef' => ['ab', 'cd', 'ef']
#
#    ("asdfadsf", ['as', 'df', 'ad', 'sf']),
#    ("asdfads", ['as', 'df', 'ad', 's_']),
#    ("", []),
#    ("x", ["x_"]),


def solution(s):
    # Ensure there are an even number of elements 
#    l = list(s)
#    if len(l) % 2: l.append("_")  
    if len(s) % 2: s = s + "_"

    # Group elements into pairs in new list
    new_list = []
#    for j in range(int(len(l) / 2)):
#        new_list.append(l[2*j] + l[2*j + 1])
    for j in range(0, len(s), 2):
        new_list.append(s[j:j+2])

    return new_list
    

def test_null():
    assert solution("") == []

def test_abc():
    assert solution('abc') ==  ['ab', 'c_']

def test_abcdef():
    assert solution('abcdef') ==  ['ab', 'cd', 'ef']

def test_asdfadsf():
    assert solution("asdfadsf") ==  ['as', 'df', 'ad', 'sf']

def test_asdfads():
    assert solution("asdfads") == ['as', 'df', 'ad', 's_']

def test_x():
    assert solution("x") == ["x_"]
