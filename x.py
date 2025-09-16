import numpy as np
import random as rd
arr_1=np.random.randint(1,10 ,size=(5,5))
print(arr_1)
arr= np.array([[1, 2, 3, 4, 5],
               [6, 7, 8, 9, 10],
               [11, 12, 13, 14, 15],
               [16, 17, 18, 19, 20],
               [21, 22, 23, 24, 25]])
print(arr)
print(arr.shape)  # shape of the array
print(arr.ndim)  # number of dimensions
print(arr.size)  # total number of elements
print(arr.dtype)  # data type of elements
print(arr.itemsize)  # size of each element in bytes
print(np.sum(arr))  # sum of all elements
print(np.sum(arr, axis=0))  # sum of each column
print(np.sum(arr, axis=1))  # sum of each row
print(np.mean(arr))  # mean of all elements
print(np.median(arr))  # median of all elements
print(np.std(arr))  # standard deviation of all elements
print(np.var(arr))  # variance of all elements
print(np.max(arr))
print(np.min(arr,axis=0))  # minimum element
print(np.min(arr,axis=1))  # minimum element
print(np.max(arr))  # maximum element
print(np.reshape(arr,(25,1)))  # reshaping the array
print(np.transpose(arr))  # transposing the array
print(arr.flatten())  # flattening the array
print(np.sort(arr, axis=0))  # sorting each column
print(np.sort(arr, axis=1))  # sorting each row
