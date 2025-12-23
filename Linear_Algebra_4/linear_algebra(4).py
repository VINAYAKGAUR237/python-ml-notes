'''                                 Linear Algebra                                     '''
'''Branch of maths that analyzes linear eqs.s, vectors, matrices, linear transformations
    Applications are in: Physics, Engineering, Coding, Machine Learning 
    Lin Alg data is represented as Scalars, Vectors and Matrices
    
Scalar --> 0 dimensional object & representes Magnitude (eg: Length, speed, weight)
            Geometrically, it is a Point

Vector --> 1 dimensional object & represents Direction & Magnitude (eg: Wind Velocity, Gravity)
            Geometrically, it is a Line with Direction

We can convert Vector to Scalar (by extracting magnitude) using norm() func            
'''

'''Vector Operations: '''
#Adding 2 vectors: Resultant of 2 vectors
#Multiplying 2 vectors --> Dot Product (cos) , Cross Product(sin)

import numpy as np

a = [4,6,7]
b = [8,9,2]

#dot product --> result is always Scalar (aka Scalar Product)
np.dot(a, b)            #100

#cross product --> result is always Vector(aka Vector Product)
np.cross(a, b)          #[-51  48 -12]

'''Dot Product:
        Mathematical Applications: 
                a) Finding angle between Vectors
                b) Project a vector onto another 
        
        Machine Learning Applications:
                a) Used in Neural Networks(deep learning)
                b) Word Embedding (Natural Language Processing)
                c) Cosine similarity(Recommendation Systems)


    Cross Product: Resulting vector is always Perpendicular(in 3D space) to input vectors 
        Mathematical Applications: 
                a) Finding angle between Vectors
                b) Project a vector onto another 
        
        Machine Learning Applications:
                a) Computer Vision --> help calculate orientation of object in 3D space
                b) Self Driving Cars --> object detection 
                c) Cosine similarity(Recommendation Systems)
'''

'''Norm of a Vector: --> Resultant Magnitude of vector (physics wala resultant magnitude) 
    It calculates magnitude of a vector i.e., Measurement of its Length
    Cuz it is Length --> it is always Positive 
    Machine Learning Applications: 
                    a) Regularization process --> helps reduce overfitting of a model
                    b) Clustering Analysis --> measuring distances between data points
    
    Formula to calculate Norm of a vector --> Resultant  underroot(a^2 + b^2 + c^2)   
'''

a = [7,5,8]
#we have to calculate norm using submodule of numpy --> linalg  (stands for linear algebra)
np.linalg.norm(a)               #11.747340

#we can use norm to calculate direction of a vector --> Unit Vector
unit_vector = a/(np.linalg.norm(a))         # --> gives dirnx in 3D space(x,y,z axis)
#             |         |
#        (vector)   (magnitude of vector)



'''Matrices : rectangular array of numbers arranged in columns and rows  --> 2D 

A multi-dimensional matrix is called a Tensor --> a ml library called TensorFlow exists this library helps process these(images --> also tensors of r,g,b) 

Matrix Operations: 
        Element wise Multiplication & Dot Product :
        Applications:
                a) Neural Networks
                b) Attention Mechanism & Transformer Models --> building block of ChatGPTs
                c) 

'''
a = np.array([[[5,6,7],[3,4,8],[6,6,9]]])
b = np.array([[[1,2,7],[3,8,9],[0,1,3]]])

#matrix multiplication (row and column jump method): --> matmul
np.matmul(a, b)
# [[[ 23  65 110]
#   [ 15  46  81]
#   [ 24  69 123]]]

#different syntax, same output:
a @ b

#dot product:
np.dot(a,b)
# [[[ 23  65 110]
#   [ 15  46  81]
#   [ 24  69 123]]]

'''Rank Of a Matrix --> count of rows that are not completely 0 
        ML Applications:
                a) Dimesionality Reduction (PCA)
                b) Feature Selection
                c) Ranking Algorithms
                d) Image Compression
                
To calculate rank we have 2 steps:
        a) Convert Matrix to Row Echelon Form  --> only goal is to make lower left triangle in matrix = all 0's
        b) Count no.of Non-zero rows        
        
 '''

#Rank of matrix: --> np.linalg.matrix_rank()
m = np.array([[1,2,3],
                [4,5,6],
                   [7,8,9]])

print("Rank of matrix 'm' =",np.linalg.matrix_rank(m))          #2

'''Determinant & Trace Of Matrices:

Determinant --> scalar value representation (quantity) that is a func of elements of matrix
        Applications:
                a) Solve Linear Eq.s
                b) Model Optimization

        eg: For 2x2 matrix:  A = [a b]  then det(A) or |A| = (ad - bc)
                                 [c d]

            For 3x3 matrix : remeber that sign changes alternatively

Trace --> sum of its diagonal elements (it should be a square matrix)
'''

#Determinant Of Matrix: --> np.linalg.det()
print("Determinant of matrix: ", np.linalg.det(m))              #0


#Trace Of Matrix: --> np.linalg.
print("Trace of matrix: ", np.trace(m))                         #15

'''Identity Matrix(I) --> it is a square matrix that when multiplied by another matrix
                          gives the other matrix in result
                           I x N = N x I = N 
                           Similar to '1' of multiplication 
                Diagonals elements = 1
                Non-diagonals elements = 0

        Applications:
                a) Neural Network - weigth initialisation
                b) Neural Network - Residual Connections'''

#Identity Matrix:
np.identity(3)
#           |
#     order of matrix req 

'''Inverse of a Matrix: A^-1  
        A X (A^-1) = I  --> Identity Matrix    '''
#Inverse of Matrix --> np.linalg.inv(m)
np.linalg.inv(m)

'''Eigen Value & Eigen Vectors 
                        A.X = lambda.X                  
(square matrix).(eigen vector) = (eigen value).(eigen vector)
                        
Eigen Values (lambda) --> set of scalar values used to represent linear eq.s in matrix operations
Imagine having to compress a box in one direction, eigen value tells you how much we can compress along specified dirxn

Applications: a) Dimensionality reduction (principle component analysis)
              b) Data Compression --> but we lose data
'''


















































































































































