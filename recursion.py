def PRINT(n):
    k=1
    if k<n:
        print(k)
        PRINT(k+1)
    else:
        return n
a=int(input("enter the range"))
PRINT(a)
