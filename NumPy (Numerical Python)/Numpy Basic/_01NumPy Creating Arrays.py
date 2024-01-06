import numpy
import numpy as np
print(np.__version__)

#type
arr=np.array((1,2,3,4,5,6))
print(type(arr))

#0-D array
print(np.array((45)))


#1-D array
arr=np.array((1,2,3,4,5,6))
print(arr)

#2-D array
print(np.array([[1,2,3],[4,5,6]]))
             #or
#print(np.mat([[1, 2, 3],[4, 5, 6]]))

#3-D array
print( np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]]))

#Check Number of Dimensions ==> keyword(ndim)
print(np.ndim(np.array((45))),"Dimensions")
print(np.ndim(np.array((1,2,3,4,5,6))),"Dimensions")
print(np.ndim(np.array([(1,2,3,4,5,6),(1,2,3,5,6,7)])),"Dimensions")
print(np.ndim(np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])),"Dimensions")

#Higher Dimensional Arrays convert ==> keyworde(ndmin)
h_d_a=np.array([1],ndmin=10)
print(h_d_a)
print('number of dimensions :',h_d_a.ndim)


