import numpy as np
lst=[1, 2.0 ,3]
arr=np.array(lst)
str=arr.astype('str')
print("List : ",lst)
print("Array : ",arr)
print("String represntation of Array : ",str)
print(str.dtype)


print("\n")
lst=[[1,2,3],[4,5,6],[7,8,9]]
arr = np.array(lst,dtype='int32')
print(arr)
print("Data type is:",arr.dtype)


print("\n")
print("Number of rows and columns of array in Q2:",arr.shape)


print("\n")
from numpy import random
print("Random numbers between 1 and 100 are:")
for i in range(10):
   x=random.randint(0,100)
   print(x)


