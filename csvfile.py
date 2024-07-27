import csv
f=open("Stu.csv","w",newline='')
stu=csv.writer(f)
stu.writerow(['Roll no', 'Name', 'Marks'])
for i in range(5):
    print("Student Record",(i+1))
    roll=int(input("Roll"))
    name=input("Name")
    marks=float(input("Marks"))
    stur=[roll,name,marks]
    stu.writerow(stur)
f.close()
