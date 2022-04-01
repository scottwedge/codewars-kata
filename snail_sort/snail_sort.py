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
    print("DEBUG ___ top snail_map is:", snail_map)
    added = snail_map.pop(0)
    print("DEBUG ___ top added= ", added)
    return added

def get_right(snail_map):
    print("DEBUG ___ right snail_map is:", snail_map)
    added = []
    for j in snail_map:
        added.append(j.pop(-1))
    print("DEBUG ___ right added= ", added)
    return added
        
def get_bottom(snail_map):
    print("DEBUG ___ bottom snail_map is:", snail_map)
    added = snail_map.pop(-1)  # Get last list 
    print("DEBUG ___ bottom pre-reverse added= ", added)
    added.reverse()
    print("DEBUG ___ bottom after reverse added= ", added)
    return added   # And reverse it

def get_left(snail_map):
    print("DEBUG ___ left snail_map is:", snail_map)
    added = []
    for j in snail_map:
        added.append(j.pop(0))
        print("DEBUG ___ get_left added= ", added)
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
    
    while True:
        added = get_top(snail_map)
        for j in added:
            result.append(j)
        print("DEBUG____ result = ", result)
    
        if len(result) == num ** 2:
            break
    
        added = get_right(snail_map)
        for j in added:
            result.append(j)
        print("DEBUG____ result = ", result)
    
        added = get_bottom(snail_map)
        print("DEBUG ____ bottom to add is: ",added)
        for j in added:
            result.append(j)
        print("DEBUG____ result = ", result)
    
#        num = num - 1
    
        added = get_left(snail_map)
        for j in added:
            result.append(j)
        print("DEBUG____ result = ", result)
    
    return (result, snail_map)

def main():
    snail_map = [[1,2,3],
         [8,9,4],
         [7,6,5]]

    print(snail_map[0])
    print(snail_map[1])
    print(snail_map[2])

    (result,remainder) = snail(snail_map)
    print("RESULT= ",result)
    print("REMAINDER= ", remainder)  #DEBUG

if __name__ == "__main__":
    main()
