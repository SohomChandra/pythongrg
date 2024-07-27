def dtb(n):
    if n==0:
        return 0
    else:
        return dtb(n//2)*10+n%2
dec=int(input("Enter the decimal no"))
print(dtb(dec))
