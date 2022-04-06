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

def test_convert_fracts_1():
    lst = [[1,2],[1,4],[1,8],[1,5]]
    assert convert_fracts(lst) == [[20,40],[10,40],[5,40],[8,40]]

def test_convert_fracts_2():
    lst = [[2,7],[1,3],[1,12]]
    assert convert_fracts(lst) == [[24,84], [28,84],[7,84]]

def test_large_numbers():
    lst = [[27115, 5262],[87546, 11111111], [43216, 255689]] == [[77033412951888085, 14949283383840498], [117787497858828, 14949283383840498], [2526695441399712, 14949283383840498]]


def convert_to_common_denom(common_d, lst):
    list_w_common_denom = []    
    for j in lst: 
        list_w_common_denom.append([int(common_d *j[0]/j[-1]), common_d])
    return list_w_common_denom


def create_list_of_numer(lst):
    list_of_numerator = []
    for j in lst:
        list_of_numerator.append(j[0])
    return list_of_numerator 

def make_d(lst):  # Calculate denominator value by multiplying all values/factors in list
    result = 1
    for j in lst:
        result = result * j
    return result
    

def create_common_denom(lst):  
    denom_list_of_factors = list()  # Init list with first value
    denom_list_of_factors = []  # Init list as empty
    for j in lst:
        d = make_d(denom_list_of_factors)  # Recalculate denominator 
        val = factor_num(j,[]) 
        for k in val: 
            if d % k == 0: 
                d = d // k  # Reduce denom
            else:
                denom_list_of_factors.append(k)  # Add factor to list
    result =  make_d(denom_list_of_factors) 
    return result


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
    list_of_denom = create_list_of_denom(lst)  # Create list of all denominators
    common_d = create_common_denom(list_of_denom)  # Calculate smallest common denominator
    list_of_numerator = create_list_of_numer(lst)
    list_w_common_denom = convert_to_common_denom(common_d, lst)
    return list_w_common_denom
