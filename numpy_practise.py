import numpy as np

# print(np.__version__)

#To create an ndarray, we can pass a list, tuple or any array-like object into the array() method, and it will be converted into an ndarray:
# arr = np.array((1, 2, 3, 4, 5))
# arr1 = np.array(42) #0D array
# arr2 = np.array([1, 2, 3, 4, 5])#1D array
# arr3 = np.array([[1, 2, 3], [4, 5, 6]]) #2D array
# arr4 = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]]) #3D array
# print(arr1)
# print(arr2)
# print(arr3)
# print(arr4)

# a = np.array(42)
# b = np.array([1, 2, 3, 4, 5])
# c = np.array([[1, 2, 3], [4, 5, 6]])
# d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

# print(a.ndim)
# print(b.ndim)
# print(c.ndim)
# print(d.ndim)
#output
# 0
# 1
# 2
# 3

# arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

# print(arr[0, 1, 2])

#Access the third element of the second array of the first array: 6

# 

# arr = np.array([1, 2, 3, 4, 5, 6, 7])

# print(arr[-3:-1])

# [5,6]
#From the second element, slice elements from index 1 to index 4 (not included):
# arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

# print(arr[1, 1:4]) [7,8,9]
# From both elements, return index 2:
# arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

# print(arr[0:2, 2]) [3,8]

# From both elements, slice index 1 to index 4 (not included), this will return a 2-D array:
# arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

# print(arr[0:2, 1:4])
# [[2 3 4]
#  [7 8 9]]

# Below is a list of all data types in NumPy and the characters used to represent them.

# i - integer
# b - boolean
# u - unsigned integer
# f - float
# c - complex float
# m - timedelta
# M - datetime
# O - object
# S - string
# U - unicode string
# V - fixed chunk of memory for other type ( void )

# 

# arr = np.array([1, 2, 3, 4], dtype='S')

# # print(arr)
# print(arr.dtype)


# Change data type from float to integer by using 'i' as parameter value:

# arr = np.array([1.1, 2.1, 3.1])

# newarr = arr.astype('i')

# print(newarr)
# print(newarr.dtype)

# The Difference Between Copy and View
# The main difference between a copy and a view of an array is that the copy is a new array, and the view is just a view of the original array.

# The copy owns the data and any changes made to the copy will not affect original array, and any changes made to the original array will not affect the copy.

# The view does not own the data and any changes made to the view will affect the original array, and any changes made to the original array will affect the view.

# arr = np.array([1, 2, 3, 4, 5])
# x = arr.copy()
# arr[0] = 42

# print(arr)
# print(x)
# [42  2  3  4  5]
# [1 2 3 4 5]

# arr = np.array([1, 2, 3, 4, 5])
# x = arr.view()
# arr[0] = 42

# print(arr)
# print(x)


arr = np.array([1, 2, 3, 4, 5])

x = arr.copy()
y = arr.view()

print(x.base)
print(y.base)