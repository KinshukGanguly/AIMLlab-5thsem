n=int(input("enter number"))
copy=n
s=0
while n>0:
 print(n%10)
 s=s*10+n%10
 n=n//10

print("Is palindrome:",copy==s)

 

