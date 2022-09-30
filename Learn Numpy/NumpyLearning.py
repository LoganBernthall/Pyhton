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
print("   ")#Adding whitespace only
#Exercise 3 - Identity Matrix, creating an identity matrix of a 4 by 4 dimension

IdentityMatrix = np.eye(4)
print(IdentityMatrix)

print("   ")#Adding whitespace only
#Exercise 4 - Array re-dimensioning, converting a 1-D array to a 3-D array
ReDimension = np.array([x for x in range(27)])
ReShaped = ReDimension.reshape((3,3,3))
print(ReShaped)

#Exercise 5 - Array Datatype conversion, convert all the elements of a numpy array from float to integer 
print("   ")#Adding whitespace only

ArrayConversion = np.array([[2.5, 3.8, 1.5], [4.7,2.9,1.56]])
ArrayConverted = ArrayConversion.astype('int')
print(ArrayConverted)

#Exercise 6 - Obtaining boolean array from binary array
print("   ")#Adding whitespace only

ArrayBoolean = np.array([[1,0,0], [1,1,1], [0,0,0]])
ArrayBooleanSorted = ArrayBoolean.astype('bool')
print(ArrayBooleanSorted)