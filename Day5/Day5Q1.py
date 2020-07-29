
#Question 1 :
#[0,1,2,10,4,1,0,56,2,0,1,3,0,56,0,4]
#Sort by increasing order but all zeros should be at the right hand side.


ls = [0,1,2,10,4,1,0,56,2,0,1,3,0,56,0,4]
ls.sort()
ls1 = []
ls2 = []
ls3 = []

for i in ls:
    if i == 0:
        ls1.append(i)
    if i > 0:
        ls2.append(i)
        
ls3 = ls2 + ls1

print(ls3)