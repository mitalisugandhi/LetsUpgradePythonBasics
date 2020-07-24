#Question 1 :
#Find sum of n numbers with help of while loop.


n = eval(input("Enter N number: "))
sum = 0
while(n>0):
    sum += n
    n -= 1
    
print("Sum of N number is: ", sum)