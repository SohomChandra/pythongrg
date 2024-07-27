d={}
n=int(input("enter the size"))
for i in range (0,n):
    n=input("enter the name")
    v=int(input("enter the values"))
    d[n]=v
print(d)
L=list(d.keys())
L1=list(d.values())
for i in range(0,len(L1)-1):
    for j in range(i+1,len(L1)):
        if L1[i]==L1[j]:
            print("Keys have common values are:",L[i],L[j])
            

    
