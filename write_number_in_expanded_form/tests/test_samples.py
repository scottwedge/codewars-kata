#!/usr/bin/env python3

import pytest
from write_number_in_expanded_form import *

#test.assert_equals(expanded_form(12), '10 + 2');
#test.assert_equals(expanded_form(42), '40 + 2');
#test.assert_equals(expanded_form(70304), '70000 + 300 + 4');

def test_12():
    assert expanded_form(12) == '10 + 2'

def test_42():
    assert expanded_form(42) == '40 + 2'

def test_70304():
    assert expanded_form(70304) == '70000 + 300 + 4'
