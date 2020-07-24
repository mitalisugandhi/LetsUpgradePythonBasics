#Question 2 :
#Take an integer and find whether the number is prime or not.

num=int(input("Enter any number="))
for i in range(2,num):
    if num%i==0:
        print("this is not prime no")
        break
else:
    print("this is prime no")