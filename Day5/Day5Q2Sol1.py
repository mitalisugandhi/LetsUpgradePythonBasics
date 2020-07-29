def combine(a, b):
    alist = []
    if a == [] and b == []:
        return alist
    if a != [] and b == []:
        return alist + a
    if a == [] and b != []:
        return alist + b
    if a != [] and b != []:
        if a[0] <= b[0]:
            alist.append(a[0])
            alist = alist +  combine(a[1:], b)
        if a[0] > b[0]:
            alist.append(b[0])
            alist = alist +  combine(a, b[1:])
    return alist
    
a = [10,20,40,60,70,80]
b = [5,15,25,35,45,60]

print(combine(a,b))