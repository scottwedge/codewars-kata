#!/usr/bin/env python3

# Write a function that accepts an array of 10 integers (between 0 and 9), that returns 
# a string of those numbers in the form of a phone number.

# Example
# create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"

# The returned format must be correct in order to complete this challenge.
# Don't forget the space after the closing parentheses!


# Functions

def create_phone_num(list_of_ten_int):
    num = ""
    for j in list_of_ten_int:
        num = num + str(j)
    return "({}) {}-{}".format(num[0:3], num[3:6], num[6:])


print(create_phone_num([1,2,3,4,5,6,7,8,9,0]))

