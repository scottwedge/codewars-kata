#!/usr/bin/env python3

def pick_peaks(arr):
    pos = []
    prob_peak = False
    for i in range(1, len(arr)):
        if arr[i] > arr[i-1]:
            prob_peak = i
        elif arr[i] < arr[i-1] and prob_peak:
            pos.append(prob_peak)
            prob_peak = False
    return {'pos':pos, 'peaks':[arr[i] for i in pos]}


def pick_peaks(arr):
    peak, pos = [], []
    res = { "peaks":[], "pos":[] }
    
    for i in range(1, len(arr)) :
        if arr[i]>arr[i-1] :
            peak, pos = [arr[i]], [i]
        
        elif arr[i]<arr[i-1] :
            res["peaks"] += peak
            res["pos"] += pos
            peak, pos = [], []
    
    return res



[200~def pick_peaks(arr):
    
    def add_peak(p):
        peaks["pos"].append(p)
        peaks["peaks"].append(arr[p])
        
    def is_peak(p):
        return arr[p-1] < arr[p] > arr[p+1]
        
    def is_plateau_start(p):
        return arr[p-1] < arr[p] == arr[p+1]
        
    def does_plateau_end_lower(p):
        return next((val for val in arr[p+1:] if val != arr[p]), arr[p]) < arr[p]

    peaks = {"pos":[], "peaks":[]}
    for p in range(1, len(arr)-1):
        if is_peak(p):
            add_peak(p)
        elif is_plateau_start(p) and does_plateau_end_lower(p):
            add_peak(p)
    
    return peaks



from itertools import izip
def pick_peaks(a):
    deltas = [(i, x2 - x1) for i, (x1, x2) in enumerate(izip(a, a[1:]), 1) if x1 != x2]
    indexes = [i for (i, dx1), (_, dx2) in izip(deltas, deltas[1:]) if dx1 > 0 > dx2]
    return dict(pos=indexes, peaks=[a[i] for i in indexes])



def pick_peaks(arr):
    res = {'pos': [], 'peaks': []}
    prev, cur = 0, 0
    for next in xrange(1, len(arr)):
        if arr[next] > arr[cur]:
            prev = cur
            cur = next
        elif arr[next] < arr[cur]:
            if arr[cur] > arr[prev]:
                res['pos'].append(cur)
                res['peaks'].append(arr[cur])
            prev = cur
            cur = next
    return res



def pick_peaks(arr):
  peaks = []
  pos = []
  current_pos = None
  
  for i in range(len(arr)-1):
    if arr[i] < arr[i+1]:
      current_pos = i+1
    elif arr[i] > arr[i+1] and i != 0 and current_pos is not None:
      pos += [current_pos]
      peaks += [arr[current_pos]]
      current_pos = None
      
  return {"pos":pos, "peaks":peaks}





import re

def pick_peaks(arr):
    slope = "".join("u" if b > a else "d" if a > b else "p" for a, b in zip(arr, arr[1:]))
    positions = [m.start() + 1 for m in re.finditer(r"up*d", slope)]
    peaks = [arr[pos] for pos in positions]
    return {"pos": positions, "peaks": peaks}




def pick_peaks(arr):
    peaks = {"pos":[], "peaks":[]}
    for i in range(1, len(arr)):
        next_num = next((num for num in arr[i:] if num != arr[i]), float("inf"))
        if arr[i-1] < arr[i] and next_num < arr[i]:
            peaks["pos"].append(i)
            peaks["peaks"].append(arr[i])
    return peaks


def pick_peaks(arr):
    prev_dex = prev_val = None
    result = {'pos': [], 'peaks': []}
    upwards = False
    for i, a in enumerate(arr):
        if prev_val == a:
            continue
        elif prev_val is None or prev_val < a:
            upwards = True
        else:
            if prev_dex and upwards:
                result['pos'].append(prev_dex)
                result['peaks'].append(prev_val)
            upwards = False
        prev_dex = i
        prev_val = a
    return result

