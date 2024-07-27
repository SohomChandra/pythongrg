L=[]
n=int(input("Enter the size"))
for i in range(0,n):
    a=int(input("enter the elements"))
    L.append(a)
print(L)
for i in range(1,n+1):
    for j in range (len(L)-1, -1, -1):
        if L.count(L[j])>1:
            L.pop(j)
            break
print(L)
          
