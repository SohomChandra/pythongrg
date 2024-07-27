d={}
n=int(input("enter the range"))
for i in range (0,n):
    k=input("enter the keys")
    v=int(input("enter the size"))
    d[k]=v
print(d)
L=list(d.keys())
L1=list(d.values())
d.clear()
for i in range (0,n):
    d[L1[i]]=L[i]
print(d)
