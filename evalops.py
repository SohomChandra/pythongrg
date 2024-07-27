tup=()
sum=0.0
tup=eval(input("Enter the elements"))
print(tup)
for i in tup:
    #if type(i)==int or type(i)==float:
    if isinstance(i,int) or isinstance(i,float):
        sum += i
print("Sum=",sum)
