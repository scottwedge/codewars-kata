#!/usr/bin/env python3

from highest_scoring_word import *

assert high('man i need a taxi up to ubud') == 'taxi'
assert high('what time are we climbing up the volcano') == 'volcano'
assert high('take me to semynak') == 'semynak'
assert high('aa b') == 'aa'
assert high('b aa') == 'b'
assert high('bb d') == 'bb'
assert high('d bb') == 'd'
assert high("aaa b") == "aaa"
