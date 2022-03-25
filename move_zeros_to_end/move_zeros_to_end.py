#!/usr/bin/env python3

# Moving Zeros To The End

# Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

# move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]


# Function

def move_zeros(l):
    count = 0
    new_l = []
    for j in l:
        if j == 0: 
            count = count + 1
        else:
           new_l.append(j)
    for j in range(count):
        new_l.append(0)
    return new_l


print(move_zeros([1, 0, 1, 2, 0, 1, 3]))    # returns [1, 1, 2, 1, 3, 0, 0]
