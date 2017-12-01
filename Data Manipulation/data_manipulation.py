import numpy as np

print(np.__version__)
#create a list comprising numbers from 0 to 9
L= list(range(10))
print(L)
for var in L:
    print(var,end=" ")
print("")
#converting integers to string - this style of handling lists is known as list comprehension.
[str(c) for c in L]
print([str(c) for c in L])
f=[float(c) for c in L]
print(f)

#Numpy arrays are homogeneous in nature, i.e., they comprise one data type (integer, float, double, etc.) unlike lists
print(np.zeros(10,dtype=int))
#creating a 3 row x 5 column matrix
print(np.ones((3,5), dtype=float) )
#creating a matrix with a predefined value
print(np.full((3,5),1.34))
#create an array with a set sequence
print(np.arange(0,20,2))
#create an array of even space between the given range of values
print(np.linspace(0,1,5))
#create a 3x3 array with mean 0 and standard deviation 1 in a given dimension
print(np.random.normal(0,1,(3,3)))
#create an identity matrix
print(np.eye(4))
#set a random seed
print(np.random.seed(0))
x1=np.random.randint(10,size=6)
x2=np.random.randint(10,size=(3,4))
x3=x1=np.random.randint(10,size=(3,4,5))
print("x3 ndim:", x3.ndim)
print("x3 shape:", x3.shape)
print("x3 size: ", x3.size)
('x3 ndim:', 3)
('x3 shape:', (3, 4, 5))
('x3 size: ', 60)

#The important thing to remember is that indexing in python starts at zero.
x1=np.array([7,34,56,12,34])
print(x1[0],"::",x1[4])
print(x1[-1],"::",x1[-2])

#Array Slicing
x=np.arange(10)
print("array","-->",x)

#from start to 4th position :: #from 4th position to end :: #from 4th to 6th position :: #return elements at even place
#return elements from first position step by two..#reverse the array
print(x[:5],":::",x[4:],":::",x[4:7],":::",x[: :2],":::",x[1::2],":::",x[::-1])

#Array Concatenation
