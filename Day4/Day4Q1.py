#Question 1 :
#Find all occurrence of substring in the given string
#“what we think we become; we are Python programmer”
#Print the index values.


str1 = "what we think we become; we are python programmer."
print(str1)
str2 = "we"
print(str2)
print(str1.count(str2))
print(str1.find(str2))
print(str1.rfind(str2))