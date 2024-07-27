import csv
f=open("Stu.csv","r")
stu=csv.reader(f)
for rec in stu:
    print(rec)
f.close()
