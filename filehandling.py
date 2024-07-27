import pickle
d={}
f=open('data.dat','ab')
n=int(input("Enter how many records"))
for i in range(n):
    r=int(input("Enter roll"))
    nm=input("Enter name")
    m=int(input("Enter marks"))
    d['Roll']=r
    d['Name']=nm
    d['Marks']=m
    pickle.dump(d,f)
f.close()
