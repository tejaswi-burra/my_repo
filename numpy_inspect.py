import numpy as np  

arr = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])

print("Array:\n", arr)
print("Shape:", arr.shape)        # rows x cols
print("Dimensions:", arr.ndim)    # number of dimensions
print("Data type:", arr.dtype)    # type of elements
print("Size:", arr.size)          # total number of elements
print("Item size:", arr.itemsize) # memory (bytes) of each element
print("Type of object:", type(arr))
