d={}
n=input("Enter the name")
for ch in n:
    if ch not in d:
        d[ch]=1
    else:
        d[ch]+=1
print(d)
