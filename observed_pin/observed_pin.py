#!/usr/bin/env python3

# The observed PIN
# 
# Alright, detective, one of our colleagues successfully observed our target person, Robby the robber. We followed him to a secret warehouse, where we assume to find all the stolen stuff. The door to this warehouse is secured by an electronic combination lock. Unfortunately our spy isn't sure about the PIN he saw, when Robby entered it.
# 
# The keypad has the following layout:
# 
# ┌───┬───┬───┐
# │ 1 │ 2 │ 3 │
# ├───┼───┼───┤
# │ 4 │ 5 │ 6 │
# ├───┼───┼───┤
# │ 7 │ 8 │ 9 │
# └───┼───┼───┘
#     │ 0 │
#     └───┘
# 
# He noted the PIN 1357, but he also said, it is possible that each of the digits he saw could actually be another adjacent digit (horizontally or vertically, but not diagonally). E.g. instead of the 1 it could also be the 2 or 4. And instead of the 5 it could also be the 2, 4, 6 or 8.
# 
# He also mentioned, he knows this kind of locks. You can enter an unlimited amount of wrong PINs, they never finally lock the system or sound the alarm. That's why we can try out all possible (*) variations.
# 
# * possible in sense of: the observed PIN itself and all variations considering the adjacent digits
# 
# Can you help us to find all those variations? It would be nice to have a function, that returns an array (or a list in Java/Kotlin and C#) of all variations for an observed PIN with a length of 1 to 8 digits. We could name the function getPINs (get_pins in python, GetPINs in C#). But please note that all PINs, the observed one and also the results, must be strings, because of potentially leading '0's. We already prepared some test cases for you.
# 
# Detective, we are counting on you!

# expectations = [('8', ['5','7','8','9','0']),
#                ('11',["11", "22", "44", "12", "21", "14", "41", "24", "42"]),
#                ('369', ["339","366","399","658","636","258","268","669","668","266","369","398","256","296","259","368","638","396","238","356","659","639","666","359","336","299","338","696","269","358","656","698","699","298","236","239"])]

def test_8():
    assert get_pins("8") ==  ('8', ['5','7','8','9','0'])

def test_11():
    assert get_pins("11") ==  ('11',["11", "22", "44", "12", "21", "14", "41", "24", "42"])

def test_369():
    assert get_pins("369") ==   ('369', ["339","366","399","658","636","258","268","669","668","266","369","398","256","296","259","368","638","396","238","356","659","639","666","359","336","299","338","696","269","358","656","698","699","298","236","239"])


def generate_pins_list(observed, possibles):
    list_of_pins = []
    if len(observed) == 1: list_of_pins = possibles[0]
    elif len(observed) == 2:
        for j in possibles[0]:
            for k in possibles[1]:
                val = str(j) + str(k)
                list_of_pins.append(val)
    elif len(observed) == 3:
        for j in possibles[0]:
            for k in possibles[1]:
                for m in possibles[2]:
                    val = str(j) + str(k) + str(m)
                    list_of_pins.append(val)
    else:
        pass
    return list_of_pins


def get_possibles(n):
    if n == "1": return ["1","2","4"]
    elif n == "2": return ["1","2","3","5"]
    elif n == "3": return ["2","3","6"]
    elif n == "4": return ["1","4","5","7"]
    elif n == "5": return ["2","4","5","6","8"]
    elif n == "6": return ["3","5","6","9"]
    elif n == "7": return ["4","7","8"]
    elif n == "8": return ["5","7","8","9","0"]
    elif n == "9": return ["6","8","9"]
    elif n == "0": return ["0","8"] 
    else: 
        return ["blah"]  # Should never get here



def to_chars(pin):  # Convert input string to list of characters (ie "0456" to ["0","4","5","6"])
    chars = []
    for j in range(len(pin)): 
        letter = pin[j:j+1]        
        chars.append(letter)
    return chars


def get_pins(observed):
    chars = to_chars(observed)
    possibles = []
    for j in chars:
        possibles.append(get_possibles(j))
    list_of_pins = generate_pins_list(observed, possibles)
    return list_of_pins
