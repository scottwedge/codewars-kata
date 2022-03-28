#!/usr/bin/env python3

from split_strings import *
    

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
