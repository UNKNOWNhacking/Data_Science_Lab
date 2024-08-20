import numpy as np 

arr = np.array([[ 1, 2, 3], [ 4, 2, 5]])
print("Array is of type: ", type(arr)) 
print("No. of dimensions: ", arr.ndim) 
print("Shape of array: ", arr.shape) 
print("Size of array: ", arr.size) 
print("Array stores elements of type: ", arr.dtype)
print("\n---------------------------------------------------------------------\n")

#Program to Perform Array Slicing

a = np.array([[1,2,3],[3,4,5],[4,5,6]])  
print(a)   
print("After slicing") 
print(a[1:]) 
print("\n---------------------------------------------------------------------\n")

#Program to Perform Array Slicing 

a = np.array([[1,2,3],[3,4,5],[4,5,6]])  
print('Our array is:' ) 
print(a) 
print('The items in the second column are:'  ) 
print(a[...,1])  
print('\n'  ) 
print ('The items in the second row are:' ) 
print(a[1,...])  
print('\n'  ) 
print('The items column 1 onwards are:' ) 
print(a[...,1:])