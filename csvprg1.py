import csv
f=open("Stu.csv","r")
stu=csv.reader(f)
for rec in stu:
    for val in rec:
        print(val,end='\t')
        
    print()
f.close()
