def move_zeros(arr):
    l = [i for i in arr if isinstance(i, bool) or i!=0]
    return l+[0]*(len(arr)-len(l))

def move_zeros(array):
    return sorted(array, key=lambda x: x==0 and type(x) is not bool)

def move_zeros(array):
    return sorted(array, key=lambda x: x == 0 and x is not False)


def move_zeros(array):
    newarr =[]
    zeroarr=[]
    for item in array:
        if item!= 0 or type(item)== bool :
            newarr.append(item)
        else:
            zeroarr.append(item)
            
            
    newarr.extend(zeroarr)
    return(newarr)
