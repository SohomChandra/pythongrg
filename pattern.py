s='*'
i=2
while i!=1:
    if i<=5:
        print(s)
        s+='*'
        i+=1
    else:
        s=s[1::]
        print(s)
        i-=1
