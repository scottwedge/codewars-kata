
from itertools import product
ADJACENTS = ('08', '124', '2135', '326', '4157', '52468', '6359', '748', '85790', '968')

def get_pins(observed):
    return [''.join(p) for p in product(*(ADJACENTS[int(d)] for d in observed))]


adjacents = {
  '1': ['2', '4'],
  '2': ['1', '5', '3'],
  '3': ['2', '6'],
  '4': ['1', '5', '7'],
  '5': ['2', '4', '6', '8'],
  '6': ['3', '5', '9'],
  '7': ['4', '8'],
  '8': ['5', '7', '9', '0'],
  '9': ['6', '8'],
  '0': ['8'],
}

def get_pins(observed):
  if len(observed) == 1:
    return adjacents[observed] + [observed]
  return [a + b for a in adjacents[observed[0]] + [observed[0]] for b in get_pins(observed[1:])]



def get_pins(observed):
  map = [['8','0'], ['1','2','4'], ['1','2','3','5'], ['2','3','6'], ['1','4','5','7'], ['2','4','5','6','8'],
         ['3','5','6','9'], ['4','7','8'], ['5','7','8','9','0'], ['6','8','9']]
  return map[int(observed[0])] if len(observed) == 1 else [x + y for x in map[int(observed[0])] for y in get_pins(observed[1:])]



from itertools import product

PIN = {'1': ('1', '2', '4'), 
       '2': ('1', '2', '3', '5'), 
       '3': ('2', '3', '6'), 
       '4': ('1', '4', '5', '7'), 
       '5': ('2', '4', '5', '6', '8'), 
       '6': ('5', '6', '9', '3'), 
       '7': ('4', '7', '8'), 
       '8': ('7', '5', '8', '9', '0'), 
       '9': ('6', '8', '9'), '0': ('0', '8')}

def get_pins(observed):
    return [''.join(a) for a in product(*(PIN[b] for b in observed))]


from itertools import product

# Map a keypad number to the nearby numbers (including the number itself).
keypad_neighbors = {
    '1': ['1', '2', '4'],
    '2': ['1', '2', '3', '5'],
    '3': ['2', '3', '6'],
    '4': ['1', '4', '5', '7'],
    '5': ['2', '4', '5', '6', '8'],
    '6': ['3', '5', '6', '9'],
    '7': ['4', '7', '8'],
    '8': ['0', '5', '7', '8', '9'],
    '9': ['6', '8', '9'],
    '0': ['0', '8']
}

def get_pins(observed):
    # Build a 2D array of possibilities
    # Each row in the array is an entry
    # Each column is a possible number.
    pins = []
    for num in observed:
        pins.append(keypad_neighbors[num])
    
    # Generate every permutation of the possible numbers.
    for tup in product(*pins):
        yield ''.join(tup)



from itertools import product

PINS = {'1': '124', '2': '1253', '3': '236', '4': '1457', '5': '24568',
        '6': '3569', '7': '478', '8': '57890', '9': '689', '0': '08'}

def get_pins(observed):
    return list(map(''.join, product(*[PINS[num] for num in observed])))
