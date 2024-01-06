import numpy as np

#Access Array Elements
arr = np.array([1, 2, 3, 4])
print(arr[0])
print(arr[1])
print("array add",arr[2]+arr[3])
print("<---------------------->")
#Access 2-D Arrays
arr_2 = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print("Dimensions:",arr_2.ndim)
print('2nd number on 1st row: ', arr_2[0,1])
print("0 colom all elament print:",arr_2[0,])
print("1 colom all elament print:",arr_2[1,])
print("<------------------------------>")
#Access 3-D Arrays
arr_3 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print("Dimensions:",arr_3.ndim)
print(arr_3)
print("index [0,0,0] to value:",arr_3[0,0,0])
print("index [1,1,0] to value:",arr_3[1,1,0])
print("<------------------------------->")
# 2d array Negative Indexing

arr_negative_d2 = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('Last element from 2nd dim: ', arr_negative_d2[1, -1])

# 3d array Negative Indexing

arr_negative_d3 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print("fast element from 3nd dim:",arr_negative_d3[0,0,-3])