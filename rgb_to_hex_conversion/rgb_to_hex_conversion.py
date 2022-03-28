#!/usr/bin/env python3

#RGB To Hex Conversion

#The rgb function is incomplete. Complete it so that passing in RGB decimal values will result in a hexadecimal representation being returned. Valid decimal values for RGB are 0 - 255. Any values that fall out of that range must be rounded to the closest valid value.

#Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.

#The following are examples of expected output values:
#rgb(255, 255, 255) # returns FFFFFF
#rgb(255, 255, 300) # returns FFFFFF
#rgb(0,0,0) # returns 000000
#rgb(148, 0, 211) # returns 9400D3

def check_limits(n):
    if n < 0: return 0
    elif n > 255: return 255
    else: return n


def rgb(r, g, b):
    text = ""
    for j in r, g, b:
        j = check_limits(j)  # Ensure value is 0-255 range
        text += hex(j).upper().replace("X","")[-2:]  # Convert '0xfe' to upper case, take only last two char
    return text
