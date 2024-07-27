l=[1,2,3,4,5]
p=l# shallow copy
print(p)
print(l)
l[0]=56
print(l)
print(p)
k=list(l)# deep copy
print(k)
print(l)
l[0]=66
print(l)
print(k)

