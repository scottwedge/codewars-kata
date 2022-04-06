

import math
import functools

def convertFracts(lst):
    lcm = lambda a, b : abs(a*b) // math.gcd(a, b)
    tmp_list = list(map(lambda x : x[1] ,list(lst)))
    lcm_num = functools.reduce(lcm,tmp_list)
    return list(map(lambda x : [x[0] * lcm_num // x[1], lcm_num] , list(lst)))
    


from fractions import gcd
def convertFracts(lst):
    D = 1
    for _,d in lst:
        D*= d//gcd(d,D)
    return [[D*n//d,D] for n,d in lst]



def convertFracts(lst):
    e = 1
    for i in lst:
        e = lcm(e, i[1])
    return [[int(e/i[1])*i[0], e] for i in lst]
    
def gcd(a,b): 
    if a == 0: 
        return b
    return gcd(b % a, a) 
    
def lcm(a,b): 
    return (a*b) / gcd(a,b)




from functools import reduce
from fractions import gcd

def convertFracts(lst):
    lcm = lambda x, y: x*y//gcd(x, y)
    D = reduce(lcm, (d for _, d in lst))
    return [[n*D//d, D] for n, d in lst]






from functools import reduce

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def lcm(a, b):
    # lcm = (a * b) / gcd(args)
    # to prevent overflow, a is computed first and then get multiplied with b
    return (a // gcd(a, b)) * b


def convertFracts(lst):
    common_denominator = reduce(lambda a, b: lcm(a, b), map(lambda arr: arr[1], lst))
    return [[a * (common_denominator // b), common_denominator] for [a, b] in lst]







def convertFracts(lst):
    lcm = 0
    returns = []
    
    for (numer, denom) in lst:
        if not lcm: lcm = denom
        else:
            a = lcm
            b = denom
            tmp = denom
            
            while b:
                if a > b: a = a - b
                else: b = b - a
                
            lcm = (lcm * tmp) // a
            
    for (numer, denom) in lst:
        e = lcm // denom
        q = numer * e
        pair = [q, lcm]
        returns.append(pair)
        
    return returns



from math import gcd

def convertFracts(lst):
    if lst == []: return []
    
    denominators = []
    for duo in lst:
        denominators.append(duo[1])
    
    lcm = denominators.pop(0)
    for denominator in denominators:
        lcm = lcm * denominator // gcd(lcm, denominator)
        
    return [[lcm//duo[1]*duo[0], lcm] for duo in lst]
