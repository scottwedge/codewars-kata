def delete_nth(order,max_e):
    ans = []
    for o in order:
        if ans.count(o) < max_e: ans.append(o)
    return ans


def delete_nth(order, max_e):
    d = {}
    res = []
    for item in order:
      n = d.get(item, 0)
      if n < max_e:
        res.append(item)
        d[item] = n+1
    return res


from collections import defaultdict

def delete_nth(order,max_e):
    c = defaultdict(int)
    def count(x):
        c[x] += 1
        return c[x] <= max_e
    return filter(count, order)


def delete_nth(order,max_e):
    answer = []
    for x in order:
        if answer.count(x) < max_e:
            answer.append(x)
    return answer
