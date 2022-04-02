#!/usr/bin/env python3

# In this kata, you will write a function that returns the positions and the values of the "peaks" (or local maxima) of a numeric array.
# 
# For example, the array arr = [0, 1, 2, 5, 1, 0] has a peak at position 3 with a value of 5 (since arr[3] equals 5).
# 
# The output will be returned as an object with two properties: pos and peaks. Both of these properties should be arrays. If there is no peak in the given array, then the output should be {pos: [], peaks: []}.
# 
# Example: pickPeaks([3, 2, 3, 6, 4, 1, 2, 3, 2, 1, 2, 3]) should return {pos: [3, 7], peaks: [6, 3]} (or equivalent in other languages)
# 
# All input arrays will be valid integer arrays (although it could still be empty), so you won't need to validate the input.
# 
# The first and last elements of the array will not be considered as peaks (in the context of a mathematical function, we don't know what is after and before and therefore, we don't know if it is a peak or not).
#
# Also, beware of plateaus !!! [1, 2, 2, 2, 1] has a peak while [1, 2, 2, 2, 3] and [1, 2, 2, 2, 2] do not. In case of a plateau-peak, please only return the position and value of the beginning of the plateau. For example: pickPeaks([1, 2, 2, 2, 1]) returns {pos: [1], peaks: [2]} (or equivalent in other languages)
# 
def test_a():
    assert pick_peaks([]) == {"pos":[],"peaks":[]}

def test_b():
    assert pick_peaks([1,1,1,1]) == {"pos":[],"peaks":[]}

def test_1():
    assert pick_peaks([1,2,3,6,4,1,2,3,2,1]) == {"pos":[3,7], "peaks":[6,3]}

def test_2():
    assert pick_peaks([3,2,3,6,4,1,2,3,2,1,2,3]) == {"pos":[3,7], "peaks":[6,3]}

def test_3():
    assert pick_peaks([3,2,3,6,4,1,2,3,2,1,2,2,2,1]) == {"pos":[3,7,10], "peaks":[6,3,2]}

def test_4():
    assert pick_peaks([2,1,3,1,2,2,2,2,1]) == {"pos":[2,4], "peaks":[3,2]}

def test_5():
    assert pick_peaks([2,1,3,1,2,2,2,2]) == {"pos":[2], "peaks":[3]}

def test_6():
    assert pick_peaks([2,1,3,2,2,2,2,5,6]) == {"pos":[2], "peaks":[3]}

def test_7():
    assert pick_peaks([2,1,3,2,2,2,2,1]) == {"pos":[2], "peaks":[3]}

def test_8():
    assert pick_peaks([1,2,5,4,3,2,3,6,4,1,2,3,3,4,5,3,2,1,2,3,5,5,4,3]) == {"pos":[2,7,14,20], "peaks":[5,6,5,5]}

def test_9():
    assert pick_peaks([18, 18, 10, -3, -4, 15, 15, -1, 13, 17, 11, 4, 18, -4, 19, 4, 18, 10, -4, 8, 13, 9, 16, 18, 6, 7]) == {'pos': [5, 9, 12, 14, 16, 20, 23], 'peaks': [15, 17, 18, 19, 18, 13, 18]}

def test_10():
    assert pick_peaks([]) == {"pos":[],"peaks":[]}

def test_11():
    assert pick_peaks([1,1,1,1]) == {"pos":[],"peaks":[]}


def find_peak(arr):
    peak_pos = []  # Initialize peak position list
    for j in range(1, len(arr)-1):  # Skip first and last spots since by definition cannot be peak there
        if arr[j] > arr[j-1] and arr[j] > arr[j+1]: peak_pos.append(j)
    return peak_pos

def find_plateau(arr):
    plateau_pos = []
    for j in range(1, len(arr)-1):  # Skip first and last spots since by definition cannot be peak there
        if arr[j-1] < arr[j] and arr[j+1] == arr[j]:  # The start of a possible plateau
            for k in range(j+1, len(arr)-1):   # Check that plateau eventually decreases
                if arr[k+1] < arr[k]: 
                    plateau_pos.append(j)
                    break
                elif arr[k+1] == arr[k]: pass
                elif arr[k+1] > arr[k]: break
    return plateau_pos


def pick_peaks(arr):
    # Search for peaks list
    # If single value, this is a peak (except if in first or last spot)
    # If more than one identical value side by side, take first value (unless very first spot)

    d = dict()

    if arr == []:
        d["pos"] = []
        d["peaks"] = []
        return d  # Handle empty case

    pos = find_peak(arr)  # Add peak positions

    pos.extend(find_plateau(arr))  # Add plateau positions 

    pos.sort()  # Sort in ascending order, in place

    val = []
    for j in pos:
        val.append(arr[j])

    d["pos"] = pos
    d["peaks"] = val

    return d
