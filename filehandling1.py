import pickle
d={}
f=open('data.dat','rb')
print('Roll\tName\tMarks')
try:
    while True:
        d=pickle.load(f)
        for k in d.keys():
            print(d[k],end='\t')
        print()
except EOFError:
    f.close()
