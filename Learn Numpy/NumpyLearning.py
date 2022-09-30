import numpy as np #Importing Numpy 

#Check numpy version installed:
print(np.__version__)

#Exercise 1 - Adding two numpy arrays

Array1 = np.array([[1,2,3],[4,5,6]])
Array2 = np.array([[10,11,12], [13,14,15]])

AdditionArray = Array1 + Array2
print(AdditionArray)
#Adds the array values together in the corresponding space
print("   ")#Adding whitespace only
#Exercise 2 - Multiplying a matrix (numpy array) by a scalar

MultipliedArray = 2*Array1

print(MultipliedArray)