L=[]
n=int(input("Enter the size"))
a=0
for i in range (0,n):
    a=int(input("Enter the elements"))
    L.append(a)
print(L)
a=int(input("the no of steps to be rotated"))
while a>0:
    t=L[-1]
    for i in range (n-1,0,-1):
        L[i]=L[i-1]
    L[0]=t
    a-=1
print(L)
