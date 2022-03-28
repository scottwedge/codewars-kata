#!/usr/bin/env python3

from rgb_to_hex_conversion import *


#The following are examples of expected output values:

def test_1():
    assert rgb(255, 255, 255) == 'FFFFFF'

def test_2():
    assert rgb(255, 255, 300) == 'FFFFFF'

def test_3():
    assert rgb(0,0,0) == '000000'

def test_4():
    assert rgb(148, 0, 211) == '9400D3'

