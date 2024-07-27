def pal(n):
    p=len(n)-1
    if n=='':
        return n
    else:
        return n[p]+pal(n[0:p])
a=input("enter the word")
print(pal(a))
                        
