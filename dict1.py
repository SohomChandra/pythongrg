d={}
n=int(input("Enter the size"))
for i in range(0,n):
    name=input("Enter the name")
    d1={}
    m1=int(input("Enter the maths"))
    m2=int(input("Enter the physics"))
    m3=int(input("Enter the chemistry"))
    d1['Maths']=[m1]
    d1['Physics']=[m2]
    d1['Chemistry']=[m3]
    d[name]=d1
print(d)
print()
print('Name\tMaths\tPhysics\tChemistry')
for k in d.keys():
    print(k,end='\t')
    for val in d[k]:
      print(d[k][val],end='\t')
    print()
