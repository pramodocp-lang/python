import numpy as np

arr = np.array([1,2,3,4,5,6,7,8,9,10])


#1. Statistical Functions
#mean → average
#max → largest value
#min → smallest value
#sum → total




#Average of all elements
print("Print Mean   :", arr.mean())


#Largest value in array:
print("Print Max   :", arr.max())


#Smallest value:
print("Print Min   :", arr.min())


#Total sum:
print("Print Sum   :", arr.sum())


arr1 = np.array([10, 20, 30])
arr2 = np.array([1, 2, 3])


#NumPy performs operations element by element, not whole array at once.
print("Addition:", arr1 + arr2)
print("Subtraction:", arr1 - arr2)


#[10*1, 20*2, 30*3]
print("Multiplication:", arr1 * arr2)


#[10/1, 20/2, 30/3]
print("Division:", arr1 / arr2)

