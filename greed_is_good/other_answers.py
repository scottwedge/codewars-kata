#!/usr/bin/env python3

def score(dice): 
  sum = 0
  counter = [0,0,0,0,0,0]
  points = [1000, 200, 300, 400, 500, 600]
  extra = [100,0,0,0,50,0]
  for die in dice: 
    counter[die-1] += 1
  
  for (i, count) in enumerate(counter):
    sum += (points[i] if count >= 3 else 0) + extra[i] * (count%3)
  return sum


def score(dice):
    return dice.count(1)//3 * 1000 + dice.count(1)%3 * 100 \
           + dice.count(2)//3 * 200 \
           + dice.count(3)//3 * 300 \
           + dice.count(4)//3 * 400 \
           + dice.count(5)//3 * 500 + dice.count(5)%3 * 50 \
           + dice.count(6)//3 * 600 \



def score(dice):
    # dice scores  [1   ,   2,   3,   4, 5,   6]
    scores_3same = [1000, 200, 300, 400, 500, 600]
    scores_single = [100 ,   0,   0,   0,  50,   0]
    
    sum = 0
    for i in range(1,7):
        count_i = dice.count(i)
        sum += (count_i // 3) * scores_3same[i-1] + (count_i % 3) * scores_single[i-1]
            
    return sum


from collections import Counter as count
def score(dice):
    threes, ones, c = {1: 1000, 6: 600, 5: 500, 4: 400, 3: 300, 2: 200}, {1: 100, 5: 50}, count(dice)
    return sum((c[v]//3)*threes[v] + (c[v]%3)*ones.get(v, 0) for v in c)
