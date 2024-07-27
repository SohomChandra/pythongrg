n=int(input("Enter the max column"))
for i in range(1,n*2):
    if i<n:
        p=i
    else:
        p=n*2-i
    print('*'*p)
