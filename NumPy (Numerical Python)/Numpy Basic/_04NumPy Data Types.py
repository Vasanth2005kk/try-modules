'''
numpy data types:

i - integer
b - boolean
u - unsigned integer
f - float
c - complex float
m - timedelta
M - datetime
O - object
S - string
U - unicode String
V - fixed chunk of memory for other type(void)
'''

import numpy as np

arr = np.array([1, 2, 3, 4])
print(arr.dtype)

arr_string=np.array(["hari","vasanth","ragu"])
print(arr_string.dtype)
arr_1=np.array("vasanth")
print(arr_1.dtype)
print("<------------------------>")
#Creating Arrays With a Defined Data Type
cre_arr=np.array([1,2,3,4,5,6],dtype="f")
print(cre_arr)
print(cre_arr.dtype)
cre_arr=np.array([1,2,3,4,5,6],dtype="S")
print(cre_arr)
print(cre_arr.dtype)
print("<----------->")

'''Create an array with data type 4 bytes integer:'''
arr = np.array([1, 2, 3, 4], dtype='i4')
print(arr)
print(arr.dtype)
arr = np.array([1, 2, 3, 4], dtype='4i')
print(arr)
print(arr.dtype)

#Change data type from float to integer by using 'i' as parameter value:
arr = np.array([1.1, 2.1, 3.1])
newarr = arr.astype('i')
print(newarr)
print(newarr.dtype)

#Change data type from integer to boolean:
arr = np.array([1, 0, 3])
newarr = arr.astype(bool)
print(newarr)
print(newarr.dtype)