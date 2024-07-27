d={}
for i in range(0,3):
    c=input("enter the country name")
    w=int(input("enter the win"))
    l=int(input("enter the loss"))
    d[c]=[w,l]
print(d)
print("Wining teams")
for k in d.keys():
    if d[k][0]>0:
        a=d[k][0]/(d[k][0]+d[k][1])*100
        print(k,'\t',a)
print("Losing teams")
for k in d.keys():
    if d[k][0]==0:
        print(k)
