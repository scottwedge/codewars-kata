#!/usr/bin/env python3

#Write Number in Expanded Form

#You will be given a number and you will need to return it as a string in Expanded Form. For example:

#expanded_form(12) # Should return '10 + 2'
#expanded_form(42) # Should return '40 + 2'
#expanded_form(70304) # Should return '70000 + 300 + 4'

#NOTE: All numbers will be whole numbers greater than 0.

def get_column(n):
    # Return the column value using modulo 10 operator
    column_value = n % 10
    return column_value
    
def get_remainder(n):
    # Return the remainder using floor 10 operator
    remainder = n // 10
    return remainder

def create_text(val, column):
    return str("{} + ".format(val * 10 ** column))
    
def expanded_form(num):
    # Determine each non-zero number
    # And how many zeros follow it
    # Store column value in list
    # Then create text output 
    
    l = list()  # Initialize value

    while num > 0:
        l.append(get_column(num))
        num = get_remainder(num)
    print("DEBUG___", l)
    
    l.reverse()  # Reverse list
    print("DEBUG ___ after reverse", l)
    text = ""
    num_zero = len(l) - 1
    for j in l:
        text += create_text(j, num_zero)
        num_zero -= 1
    return text

def main():
    num = 91385
    print("DEBUG ___ starting with: ", num)
    print(expanded_form(num))

if __name__ == "__main__":
    main()
