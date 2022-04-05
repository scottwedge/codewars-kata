#!/usr/bin/env python3
# 
# Common denominators
# You will have a list of rationals in the form
# { {numer_1, denom_1} , ... {numer_n, denom_n} } or
# [ [numer_1, denom_1] , ... [numer_n, denom_n] ] or
# [ (numer_1, denom_1) , ... (numer_n, denom_n) ] 
# 
# where all numbers are positive ints. You have to produce a result in the form:
# 
# (N_1, D) ... (N_n, D) or
# [ [N_1, D] ... [N_n, D] ] or
# [ (N_1', D) , ... (N_n, D) ] or
# {{N_1, D} ... {N_n, D}} or
# "(N_1, D) ... (N_n, D)"
# 
# depending on the language (See Example tests) in which D is as small as possible and
# 
# N_1/D == numer_1/denom_1 ... N_n/D == numer_n,/denom_n.
# 
# Example:
# convertFracs [(1, 2), (1, 3), (1, 4)] `shouldBe` [(6, 12), (4, 12), (3, 12)]
# 
# Note:
# Due to the fact that the first translations were written long ago - more than 6 years - these first translations have only irreducible fractions.
# 
# Newer translations have some reducible fractions. To be on the safe side it is better to do a bit more work by simplifying fractions even if they don't have to be.
# 
# try:
#     from solution import convert_fracts
# except:
#     from solution import convertFracts as convert_fracts
#     
# @test.describe("Basic tests")
# def f():
#     @test.it("should pass basic tests")
#     def f():
#         a = []
#         b = []
#         test.assert_equals(convert_fracts(a), b)
#         a = [[1, 2], [1, 3], [1, 4]]
#         b = [[6, 12], [4, 12], [3, 12]]
#        test.assert_equals(convert_fracts(a), b)

def test_30():
    assert factor_num(30, []) == [2,3,5]

def test_121():
    assert factor_num(121, []) == [11,11]

def test_create_denom_60():
    assert create_common_denom([2,3,4,5])  == 60
 

def make_d(l):  # Calculate denominator value by multiplying all values/factors in list
    result = 1
    for j in l:
        result = result * j
    return result
    

def create_common_denom(lst):  
    denom_list_of_factors = [1]
    d = 1
    for j in lst:
        d = make_d(denom_list_of_factors)  # Recalculate denominator 
        if d % j == 0: 
            d = d // j  # Reduce denom
        else:
            denom_list_of_factors.append(j)  # Add this 
            d = d * j  # Must increase 
    return make_d(denom_list_of_factors)


def factor_num(n, facts):  # Convert number 'n' to list of its factors
    if n == 1: return facts  # Return list of factors
    for j in range(2, n+1):
        if n % j == 0:
            facts.append(j)
            new_n = n // j
            return factor_num(new_n, facts)


def create_list_of_denom(lst):
    # Grab the last entry of each value pair since it is the denominator
    list_of_denom = []
    for j in lst:
        list_of_denom.append(j[-1])
    return list_of_denom


def convert_fracts(lst):
    list_of_denom = create_list_of_denom(lst)
    denom = create_common_denom(list_of_denom)
