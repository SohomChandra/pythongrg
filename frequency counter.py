L=[]
n=int(input("Enter the size"))
a=0
for i in range (0,n):
    a=int(input("Enter the elements"))
    L.append(a)
print(L)
L1=[]
for num in L:
    if num not in L1:
        L1.append(num)
        print(num,"=",L.count(num))
