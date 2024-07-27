marks=()
for i in range (0,5):
    t=()
    for j in range (0,3):
        a=int(input("Enter the marks"))
        t+=(a,)
    marks+=(t,)
print(marks)
for t in marks:
    total=sum(list(t))
    avg=total/3
    print(t,"total=",total,"Average=",avg)
    
