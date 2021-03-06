#!/usr/bin/env python3

from snail_sort import *
 
array1 = [[1,2,3],
          [8,9,4],
          [7,6,5]]
# snail(array1) #=> [1,2,3,4,5,6,7,8,9]

def test_123894765():
    assert snail(array1) == [1,2,3,4,5,6,7,8,9]


array2 = [[1,2,3],
          [4,5,6],
          [7,8,9]]
# snail(array2) #=> [1,2,3,6,9,8,7,4,5]

def test_123456789():
    assert snail(array2) == [1,2,3,6,9,8,7,4,5]


#array4x4 = 1  2  3  4
#          12 13 14  5
#          11 16 15  6
#          10  9  8  7
array4x4 = [[1,2,3,4],[12,13,14,5],[11,16,15,6],[10,9,8,7]] 

def test_4x4():
    assert snail(array4x4) == [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]


#array5x5 =  1  2  3  4  5
#           16 17 18 19  6
#           15 24 25 20  7
#           14 23 22 21  8
#           13 12 11 10  9
array5x5 = [[1,2,3,4,5], [16,17,18,19,6], [15,24,25,20,7], [14,23,22,21,8], [13,12,11,10,9]]

def test_5x5():
    assert snail(array5x5) == [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
