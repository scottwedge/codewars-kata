[200~def high(x):
    return max(x.split(), key=lambda k: sum(ord(c) - 96 for c in k))

def high(x):
    words=x.split(' ')
    list = []
    for i in words:
        scores = [sum([ord(char) - 96 for char in i])]
        list.append(scores)
    return words[list.index(max(list))]

def high(words):
    return max(words.split(), key=lambda word: sum(ord(c) - ord('a') + 1 for c in word.lower()))

def high(x):
    highest_score = 0
    for word in x.split(' '):
        score = sum(ord(c)-96 for c in word)
        if score > highest_score:
            highest_score = score
            highest_word = word
            
    return highest_word

def xx(m):
    a = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,'l':12,
             'm':13,'n':14,'o':15,'p':16,'q':17,'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26}
    n = 0
    for i in m:
        n += a[i]
    return n

def high(x):    
    x = x.split()
    m,n = x[0],xx(x[0])
    for i in x[1:]:
        if xx(i) > n:
            m = i
            n = xx(i)
    return m

def high(x):
    s, n = x.split(), [sum(ord(c) - 96 for c in y) for y in x.split()]
    return s[n.index(max(n))]
