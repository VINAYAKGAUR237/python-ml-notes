                                # Intro to NumPy 

#NumPy --> called Numerical Python; fundamental lib in Data Science Ecosystem
'''Data Object is called 'nd array' , it is a core Data Structure (n stands for n-dimensions)
Powerful Tools in NumPy:

        - Offers efficient storage for various data types like: strings, floats, etc
        - Arrays perform faster than lists 
        - NumPy offers rich set of data, mathematical and statistical operations/funcs
        - You can easily perform slicing, merging and indexing of arrays 
        - Random array or Matrix generation ie it can Generate Random Data for you
        - It is foundation of many Data Science libraries
         
          
NumPy is written in C language in background that's why its faster than Python itself '''


#Basics: 
"""To install NumPy, write command --> pip install numpy or pip3 install numpy"""
import numpy as np

#Our first array in numpy:   within brackets is a list --> converted to NumPy array --> more powerful
arr = np.array([2,4,6])

#'np' is alliace/nickname for numpy by convention cuz we will be using it as a func 

print(type(arr))  # prints 'numpy.ndarray' where ndarray is a 'NumPy Object'

#Convert List into NumPy array:
myList = [1,2,3,4,5]
arr = np.array(myList)
#OR
arr = np.array([1,2,3,4,5])


print(type(myList))
print(type(arr))


#arange() func --> this is a-range and not arrange 

r = list(range(1,4))           # [ 1,  2,  3]
a = np.arange(1,4)             # array([ 1,  2,  3])

print(type(r))                  # <class 'range'>
print(type(a))                  # <class 'numpy.ndarray'>


#Math Operation: Multiplying by 2
print(x * 2 for x in r)                     #uses for loop to multiple each element --> [2, 4, 6]
print(a * 2)                                #directly multiples each element with 2 --> array([2, 4, 6])

#That's why we use NumPy for Math and Stat works

#Increments:
np.arange(2, 41, 2)      #prints numbers from 2 to 40 with gap of 2


#Array Dimensions:

# 0-D Array (Scalar): 
a0 = np.array(40)
a0.ndim         # 0
# 'ndim'  --> n-dimension

#1-D Array (Vector/Line):
a1 = np.array([2,3,4])
a1.ndim         # 1

#2-D Array (Table/Matrix):
a2 = np.array([[1,2,3],         #1st Row
               [4,5,6]])        #2nd Row

a2.ndim         # 2

#Getting Shape of Array --> it gives Row Count & Column Count
a2.shape        # (2, 3)

#Getting Count of No.of Elements:
a2.size         # 6


#3-D Array (Cube):
a3 = np.array([[[1,2,3]                 #1st Layer
                [4,5,6]
                [7,8,9]],[[1,2,3]       #2nd Layer
                          [4,5,6]
                          [7,8,9]]])
a3.ndim         # 3

a3.shape        # (2, 3, 3) --> (2 Layers, 3 Rows, 3 Columns)

"""0-D array uses 0 square brackets
   1-D array uses 1 pair of square brackets
   2-D array uses 2 pairs of square brackets 
   3-D array uses 3 pairs of square brackets"""

#Shape func can be referenced as Object --> we can access elements of shape using Indexing 
print(f"This array has {a3.shape[0]} Layers") 
print(f"This array has {a3.shape[1]} Rows") 
print(f"This array has {a3.shape[2]} Columns") 


#Arithmetic Operations in NumPy:
arr1 = np.array([3,4,5])
arr2 = np.array([10,20,30])

#Addition:
arr1 + arr2   #[13,24,35]

#Multiplication:
arr1 * arr2    #[30, 80, 150]

#Division:
arr1 / arr2     #[0.33, 0.2, 0.16]

"""BroadCasting --> when we use arithmetic operations on 2 arrays with different dimensions 
                    then the smaller one is stretched in background to be compatible with bigger one

                                np.array([1,2,3]) * np.array(10)
                                    |                   |
                                   1D Array           0D Array

                                                |
                                                v
                                        [1,2,3] * [10,10,10]
                                                
                                                |
                                                v
                                            [10,20,30]

Similarly, 
        1D array can be added to 2D array if no.of 1D array elements matches no.of 2D array columns

Dimensions are compatible if:

They are equal, or one of them is 1
If any pair of dimensions don't follow these rules, broadcasting fails.
"""

#Reshape:
arr = np.arange(1,10)           #(1,2,3,4,5,6,7,8,9)  --> 1D array

arr_new = arr.reshape(3,3)      #([1,2,3],[4,5,6],[7,8,9]) --> 2D array
                #     | |
                #  Rows  Columns

arr_new = arr.reshape(2,2,3)      
                #   |   |   |
          #     Layers  Rows  Columns
        
"""([1,2,3],
        [4,5,6]) --> 2D array"""

#Flatening an array --> used to flatten an image pixel so that we can pass it to neural network
arr_new.reshape(-1)  # using reshape(-1) --> automatically flattens the array 
#any negative value works

#Modulus Function --> gives remainder 
a1 = np.array(10, 20, 30)
a2 = np.array(3, 4, 5)

np.mod(a1, a2)   #([1, 0, 0])

        #String/Text Arrays in NumPy:
greetings = np.array(["Hello", "Welcome"])
greetings2= np.array(["Everyone", "To The NumPy Class !!"])

#add strings:
np.char.add(greetings, greetings2)  #(["Hello Everyone", "Welcome To The NumPy Class !!"]) --> this is like Matrix Addition

#concatenation of Strings:
np.concatenate(greetings, greetings2)  #(["Hello", "Welcome", "Everyone", "To The NumPy Class !!"])

#Concatenation of Numbers:
arr1 = np.array([[10,20],
                [30,40]])

arr2 = np.array([[50,60],
                 [70,80]])

np.concatenate(arr1, arr2)             #([  [10,20],
                                        #   [30,40],
                                        #   [50,60],
                                        #   [70,80]  ])  

# This is just Stacking of Numbers on eachother


np.concatenate((arr1, arr2), axis = 0)     #concat for columns - vertical
#([  [10,20],
#    [30,40],
#    [50,60],
#    [70,80]  ])


np.concatenate((arr1, arr2), axis = 1)     #concat for columns - horizontal
#([  [10,20,30,40],
#    [50,60,70,80]  ])

#But all this concat must match for Compatibility(rows & columns)

#Additional 'Char' Functions:
        #Upper:
a = np.array(["Hello", "hELLO", "world", "worLd"])
np.char.upper(a)
# (["HELLO", "HELLO", "WORLD", "WORLD"])

        #Unique: --> this removes redundancy/repetitions
np.unique(a)
# (["HELLO", "WORLD"])

        #Replace: --> helps make data labelling consistent 
arr1 = np.array(["Model A", "Model B", "Concept C", "Concept D"])
np.char.replace(arr1, "Model", "Concept")
#(["Concept A", "Concept B", "Concept C", "Concept D"])
 
        #Strip: --> removes Whitespaces 
arr1 = np.array(["  Model A   ", "   Model B ", "  Concept C  ", "   Concept D "])
np.char.strip(arr1)
#(["Model A", "Model B", "Concept C", "Concept D"])

        #And many more funcs on NumPy Documentation



        #Statistical Functions In NumPy

#Random Func: --> generates a array with random numbers
arr_x = np.random.rand(1,10)
#                 |  |
#         dimension  elements

arr_x = np.random.randint(1,10) #this generates random 'integer' array

#Mean:
np.mean(arr_x)                  #average of number

#Median:
np.median(arr_x)                #gives middle value

#Standard Deviation:
np.std(arr_x)

#Maximum & Minimum:
np.max          #gives max 
np.max(arr,axis=0)      #this gives max for each element

#Mean for 2-D Array:
arr = ([[1,2,3],
        [10,20,30],
        [100,200,300],
        [1000,2000,3000]])

np.mean(arr)  #this gives overall one value

np.mean(arr,axis=0) #gives Mean of each Column (3)      ([277.75, 555.5, 833.25])
np.mean(arr,axis=1) #gives Mean of each Row (4)         ([1.5, 15, 150, 1500])

#Mean for 3-D Array:
a3 = np.array([[[1,2,3]                 #1st Layer
                [4,5,6]
                [7,8,9]],[[1,2,3]       #2nd Layer
                          [4,5,6]
                          [7,8,9]]])

np.mean(a3,axis=2) #this gives average in layers 
#([[2,5,8]    #row1,row2,row3
#  [2,5,8]]) 

np.mean(a3,axis=0) #directly adds element in front of eachother in layer
# ([[1,2,3]
#   [4,5,6]
#   [7,8,9]])


#Filtering in NumPy:
a = np.arange(1,31)

#get the values that are Less Than 14:
filtered_a = a[a<14]
print(filtered_a)   #([1,2,3,4,5,6,7,8,9,10,11,12,13])

#get the values that are Less Than 14 and greater than 4:
filtered_a = a[(a<14) and (a>4)]
print(filtered_a)   #([5,6,7,8,9,10,11,12,13])


#Where Func:
arr = np.array([1, 2, 3, 4, 5])

result = np.where(arr > 3, 10, 0)
#                  |        |    |
#             (cond)  (if true)  (if false)
print(result)      #[0 0 0 10 10]

#If it is Multi-condition based --> nested Where Func


#Slicing & Dicing Array (2D Array)
#Slicing --> we takes out a part of data using Indices

a = np.array([[2,3,5],
              [5,9,45],
              [15,23,4]])

''' Slicing uses Square Brackets [ ] '''

a[0,1]  #prints 9
a[1]    #prints 1st row--> [5,9,45]
a[0:2]  #prints first 2 rows --> [2,3,5] & [5,9,45]

# 0:2  --> gets us 2 rows (range)
# 0,2 --> gets us to a element(comma) -> [5]

a[-1]   #gives last row 
a[1:3]  #gives row 1 to 2
a[1:3, 1:3]     #gives row 1 to 2 & element 1 to 2

#if we want till end then no need to mention:
a[1: , 1: ]     #gives row 1 to end & element 1 to end 

#selecting all rows but from 2nd column to end column
a[ : , 1 : ]

#cuz first portion represents Rows & second portion represents Columns

#Also:
a[1,0] + a[1,1]  # 5 + 9 = 14

#Printing every second Row:
arr = np.array([[1,2,3],[4,5,6],[1,2,3],[4,5,6],[1,2,3],[4,5,6],[1,2,3],[4,5,6]])

a[1::2]  #--> print Row 1 & then Hop by 2 and print 2nd hop place

a[1::2, 1:]  #--> print Row 1 & then Hop by 2 and print 2nd hop place and do this for Column 1 till end column


#Slicing/Referencing for 3D Array:

arr = np.array([[[1,2,3],[4,5,6],[7,8,9]],                       #1st Layer
                [[10,20,30],[40,50,60],[70,80,90]]])             #2nd Layer 

#to get a slice from it --> (layer, row, column)
arr[0,2,0]         #7
arr[1,1,0:3]       #[40,50,60]


"""Generating Data in NumPy:   """

arr = np.random.rand(1,10)   #gives random no.s from 1 to 10

#For Integers:
arr = np.random.randint(1,10)   #gives random integers from 1 to 10

#For getting array of 40 elements ranging randomly btw 1 to 100
arr = np.random.randint(1,100,size = 40)

#Getting array of 40 elements ranging randomly btw 1 to 100 and store them in a matrix
arr = np.random.randint(1,100,size = (8,7))  #rows, columns

#Generate evenly spaced value using --> linspace
#Get 20 equal divisions between 0 & 1
arr = np.linspace(0,1,20)
#                |  |   |
#            start end  no.s in btw


arr = np.linspace(0,1,20,retstep = True)        #this gives us value of increment at each step 
#retstep --> means Return Step


#Loading Data from a File
arr = np.loadtxt('file_name', delimiter=',', dtype=int)   #this loads data from the given file
#                                 |             |
#                              separator    to get specific data type
#                                 (both of these are optional)


"""                               That's It For NumPy
                                  Now Going To Pandas !!                 """





