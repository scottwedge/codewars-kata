def unique_in_order(iterable):
    result = []
    prev = None
    for char in iterable[0:]:
        if char != prev:
            result.append(char)
            prev = char
    return result


from itertools import groupby
def unique_in_order(iterable):
    return [k for (k, _) in groupby(iterable)]


def unique_in_order(iterable):
    res = []
    for item in iterable:
        if len(res) == 0 or item != res[-1]:
            res.append(item)
    return res
            

unique_in_order = lambda l: [z for i, z in enumerate(l) if i == 0 or l[i - 1] != z]
