s=int(input("enter number"))
l1=[23,21,5,45,9,10]

l1.sort()
print(l1)
l=0
f=0
u=len(l1)-1

while(l<=u):
 mid=(l+u)//2
 if l1[mid]==s:
  print("element found at index",mid)
  f=1
  break
 elif l1[mid]<s:
  l=mid+1
 else:
  u=mid-1

if f==0:
 print("element notfound")
