import numpy as np
a=np.arange(4)
print(a)

a=np.insert(a,2,100)#2 is position 100 is value 
print(a)

a=np.insert(a,1,[100,101,102])#1 is position the array is the value
print(a)

a=np.insert(a,[0,2,4],[100,101,102])#100 goes to 0, 101 goes to 2,102 goes to 4th posn
print(a)

ar=np.arange(12).reshape((3,4))#creates a 3x4 matrix and fill it with 0-11
print(ar)

ar=np.insert(ar,2,100,axis=0)#inserts a row at 2nd position where all is 100
print(ar)

b=np.arange(100,104)#creates a row from 100-103
print(b)

ar=np.insert(ar,1,b,axis=0)#inserts row b in posn 1
print(ar)

a=np.arange(12).reshape((3,4))
print(a)

a=np.insert(a,1,100,axis=1)#inserts a Column at posn 1
print(a)

c=np.arange(100,103)
a=np.insert(a,1,c,axis=1)#inserts column a to posn 1
print(a)

c=np.arange(100,106).reshape(3,2)
a=np.insert(a,[1],c,axis=1)#inserts another smaller array at posn 1
print(a)

b=np.empty([3,4]).dtype=int#makes an empty matrix
print(b)

b=np.full([3,3],55,dtype=int)#makes a 3x3 matrix full of 55
print(b)

##c=input("Enter array elements separated by space")
##l=c.split()
##nparray=np.array(l,dtype=int)#inserting array from the user
##print(nparray)
##
##r=int(input("Enter the no. of rows"))
##c=int(input("Enter the no. of columns"))
##l=[]
##for i in range(r*c):
##    l.append(int(input()))
##ddarray=np.array(l).reshape(r,c)
##print(ddarray)
##
##arry=np.array([[1,2,3],[4,5,6]])
##np.save('file.npy',arry)#save the array to a file

##load_ar=np.load('file.npy')
##print(load_ar)#loads and opens the file
##
##np.savetxt('file2.txt',arry)#saves file as txt file
##load_ar=loadtxt('file2.txt')

##a=np.array([])
##ans=''
##while ans.lower()!='exit':
##    ans=input("Enter 'exit' to stop")
##    if ans.isdigit():
##        np.append(a,int(ans))
##    else:
##        print("It is not Integer, try again")
##print(a.mean)

x=np.arange(4).reshape(2,2)
y=np.arange(5,9).reshape(2,2)
z=np.array(x)+np.array(y)#adding of matrix
print(z)


