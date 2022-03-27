#!/usr/bin/env python3

#Unique In Order

#Implement the function unique_in_order which takes as argument a sequence and returns a list of items without any elements with the same value next to each other and preserving the original order of elements.

#For example:

#unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
#unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
#unique_in_order([1,2,2,3,3])       == [1,2,3]



# Functions

def unique_in_order(text):
    # Convert text to list
    # Iterate through list and only copy new unique values to new list

    if text == "":
        return []
    else:
        l = list(text)  # Init results list
        result_l = list()  # Init results list with first element
        result_l.append(l[0])
        
        for j in range(1, len(l)):
            if l[j] != l[j - 1]:
                result_l.append(l[j])  # Add this value
        return result_l
