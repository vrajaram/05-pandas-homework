import numpy as np
import pandas as pd

# Numerical Analysis with Numpy Arrays

# 1. Create your first array with the elements [1,22.4,5,35,4,6.7,3,8,40] and print it.
# Experiment what the following functions do: ndim, shape, size and dtype:

array = np.array([1, 22.4, 5, 35, 4, 6.7, 3, 8, 40])

print('Answer : 01')
print(array)
print('Ndim value:')
print(array.ndim)
print('shape value:')
print(array.shape)
print('size value:')
print(array.size)
print('dtype value:')
print(array.dtype)

# 2. Create your first matrix with the elements [['a', 'b'],['c', 'd'],[3, 3]] and print it.
# Experiment what the following functions do: ndim, shape, size and dtype:

array2 = np.array([['a', 'b'],['c', 'd'],[3, 3]])

print('Answer : 02')
print(array2)
print('Ndim value:')
print(array2.ndim)
print('shape value:')
print(array2.shape)
print('size value:')
print(array2.size)
print('dtype value:')
print(array2.dtype)

# 3. Create numpy 1 dimension array using each of the functions arange and rand

array3 = np.arange(10)
array4 = np.random.rand(10)*10

print('Answer : 03')
print(array3)
print(array4)

# 4. Create numpy 2 dimensions matrix using each of the functions zeros and rand

matrix = np.zeros((2, 2))
matrix2 = np.random.rand(2, 2)

print('Answer : 04')
print(matrix)
print(matrix2)

# 5. Create an array containing 20 times the value 7. Reshape it to a 4 x 5 Matrix

array5 = np.ones(20)*7
matrix3 = array5.reshape(4,5)

print('Answer : 05')
print(array5)
print(matrix3)

# 6. Create a 6 x 6 matrix with all numbers up to 36, then print:
# only the first element on it
# only the last 2 rows for it
# only the two mid columns and 2 mid rows for it
# the sum of values for each column

matrix4 = np.arange(36)+1
matrix4 = matrix4.reshape(6,6)

print('Answer : 06')
print(matrix4)

print('sum of each column')
print(np.sum(matrix4,axis=0))

print('First element')
print(matrix4[0,0])

print('last 2 rows')
print(matrix4[4:,:])

print('two mid columns and 2 mid rows')
print(matrix4[2:4,2:4])


