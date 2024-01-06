import numpy

#array slicing ==>  [start:end]
#array slicing ==>  [start:end:step]

arr=numpy.array([1,2,3,4,5,6,7,8,9])

print(arr[1:5])
print(arr[:5])
print(arr[3:])

#negative slicing
print(arr[-7:-2])
print(arr[-8:])
print(arr[:-3])
print("revers:",arr[::-1])

#stpe slicing
print(arr[1::2])
print(arr[1:5:3])
print(arr[-8:-1:2])
print(arr[1::4])
print(arr[::4])
print("<------------------------------->")
#Slicing 2-D Arrays

arr_2d=numpy.array([[1,2,3,4,5],[6,7,8,9,0]])
print(arr_2d[1,::-1])
print(arr_2d[0,1:4])
print(arr_2d[0,1::])
print(arr_2d[1,:3])
print(arr_2d[0,1::2])

print(arr_2d[0:3,1:6])
print(arr_2d[0:4,4])