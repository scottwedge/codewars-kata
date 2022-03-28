#!/usr/bin/env python3

#Write Number in Expanded Form

#You will be given a number and you will need to return it as a string in Expanded Form. 
#For example:

#expanded_form(12) # Should return '10 + 2'
#expanded_form(42) # Should return '40 + 2'
#expanded_form(70304) # Should return '70000 + 300 + 4'

#NOTE: All numbers will be whole numbers greater than 0.

def get_column(n):
    # Calculate the column value using modulo 10 operator
    column_value = n % 10
    return column_value
    
def get_remainder(n):
    # Calculate the remainder using floor 10 operator
    remainder = n // 10
    return remainder

def create_text(l):
    l.reverse()  # Reverse list
    num_zero = len(l) - 1
    text = "{}".format(l[0] * 10 ** num_zero)  # First number
    for j in range(1, len(l)):
        num_zero = num_zero - 1
        if l[j] != 0:
            text = text + " + {}".format(l[j] * 10 ** num_zero)  # First number
    return text
    
def expanded_form(num):
    # Determine each non-zero number
    # And how many zeros follow it
    # Store column value in list
    # Then create text output by printing first number
    # then if > 1 column print " + " and remaining numbers (if not zero) until done
    
    l = list()  # Initialize value

    while num > 0:
        l.append(get_column(num))
        num = get_remainder(num)
    
    text = create_text(l)
    return text

