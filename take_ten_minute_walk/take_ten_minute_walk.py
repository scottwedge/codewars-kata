#!/usr/bin/env python3

# You live in the city of Cartesia where all roads are laid out in a perfect grid. You arrived ten minutes too early to an appointment, so you decided to take the opportunity to go for a short walk. The city provides its citizens with a Walk Generating App on their phones -- everytime you press the button it sends you an array of one-letter strings representing directions to walk (eg. ['n', 's', 'w', 'e']). You always walk only a single block for each letter (direction) and you know it takes you one minute to traverse one city block, so create a function that will return true if the walk the app gives you will take you exactly ten minutes (you don't want to be early or late!) and will, of course, return you to your starting point. Return false otherwise.

#   Note: you will always receive a valid array (string in COBOL) containing a random assortment of direction letters ('n', 's', 'e', or 'w' only). It will never give you an empty array (that's not a walk, that's standing still!).

def is_valid_walk(walk):  #determine if walk is valid
    # Check if length of walk = 10, otherwise it is too long 
    if len(walk) == 10: valid = True  # Initialize. If any tests fail, then set this False
    else: valid = False

    # Verify same number of "e" and "w", and "n" and "s" else do not return to starting point
    d = dict()
    d["e"] = d["w"] = d["n"] = d"s"] = 0  # Init all dictionary values
    for j in walk:
        d[j] = d[j] + 1  # Increment count

    if d["e"] != d["w"]: valid = False
    if d["n"] != d["s"]: valid = False

    return valid 
