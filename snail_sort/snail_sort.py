#!/usr/bin/env python3

# Snail Sort
#
# Given an n x n array, return the array elements arranged from outermost elements to the middle element, traveling clockwise.
# 
# array = [[1,2,3],
         # [4,5,6],
         # [7,8,9]]
# snail(array) #=> [1,2,3,6,9,8,7,4,5]
# 
# For better understanding, please follow the numbers of the next array consecutively:
# 
# array = [[1,2,3],
         # [8,9,4],
         # [7,6,5]]
# snail(array) #=> [1,2,3,4,5,6,7,8,9]
# 
# This image will illustrate things more clearly:
# 
# NOTE: The idea is not sort the elements from the lowest value to the highest; the idea is to traverse the 2-d array in a clockwise snailshell pattern.
# 
# NOTE 2: The 0x0 (empty matrix) is represented as en empty array inside an array [[]]

# Functions
def get_top(snail_map):
    added = snail_map.pop(0)
    return added

def get_right(snail_map):
    added = []
    for j in snail_map:
        added.append(j.pop(-1))
    return added
        
def get_bottom(snail_map):
    added = snail_map.pop(-1)  # Get last list 
    added.reverse()
    return added   # And reverse it

def get_left(snail_map):
    added = []
    for j in snail_map:
        added.append(j.pop(0))
    added.reverse()
    return added
        

def snail(snail_map):
    # Calculate the number and size (should be equal in nxn array) of each list in array
    # Plan is to remove top/first row from left to right, 
    #   then delete that (first) list
    # Then pop last element in every list from top to bottom
    # Then pop each element in bottom/last list from right to left (ie reverse order) 
    #   and then delete that (last) list
    # Then take first element in all lists from bottom to top
    # Then repeat

    num = len(snail_map)  # Calculate length of each list and number of lists
    
    result = []
    
    while len(result) != num ** 2:
        added = get_top(snail_map)
        for j in added:
            result.append(j)
    
        if len(result) == num ** 2: break
    
        added = get_right(snail_map)
        for j in added:
            result.append(j)
    
        if len(result) == num ** 2: break
    
        added = get_bottom(snail_map)
        for j in added:
            result.append(j)
    
        if len(result) == num ** 2: break
    
        added = get_left(snail_map)
        for j in added:
            result.append(j)
    
    return result
