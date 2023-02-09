# numerical python
# it will only use integer float arrays
#  vectorisation
import numpy as np



ar1=np.array([1,2,3,4,5])
print(ar1)
print(type(ar1))

#  array use only one data type,mathematical calculations are faster in array than list

# ar2=np.array([2,3,5,6,7,1.3])
# print(ar2)

 #list
#
# l1=[1,2,3,4]
# l2=[5,6,7,8]
# a=l1+l2
# print(a) # here + symbol will concatenate it
#
# arr1=np.array([10,23,45,66])
# arr2=np.array([1,3,4,5])
# print(arr1+arr2)  # give the sum of 2 arrays

# list*3
l1=[1,2,3]
print(l1*3)# repeate the list about the multiplied times

# array*3

ar=np.array([1,2,3])
print(ar*3)

#  METRIX
b=np.array([[1,2,3],[4,5,6]])
print(b)
#
# # to print the size of the metrix
#
# print(b.shape)   # row ,col
#
# # to access a element in a metrix
# print(b[1,2])

# access first full row

# print(b[0,:])
#
# # for access col
# print(b[:,0])
#
# # access first 2 numbers ina row
#
# print(b[0,0:2])
#
# # for change the shape of metrix
#
# print(b.reshape(3,2))
#
# # transpose
# print(b.transpose())
#
