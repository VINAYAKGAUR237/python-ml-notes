
#Python is a Implicit Typed Lang i.e we dont need to define data types of variables it automatically does that

#In python '*' can operate with both numbers and strings as well 
print(2*3*"Hello Ji !!")     # prints --> Hello Ji !! 6 times 

#Similarly, '+' can operate only with 2 strings
print("Hello" + " Ji " + "!!")    # prints -->  Hello Ji !!

#Arithmetic operations on float and int --> results in float

#Result of Division operator is Float (1/2 == 0.5)

# To get floating value in integer use --> // as division operator
A = 1, B = 2
print(A / B)    # 0.5
print(A // B)   # 0.0

#take INPUT from user.
name = input("Enter Your Name: ")

#Typecasting of user input 
name = int(input("Enter 1st Number: "))
name = float(input("Enter 1st Number: "))
name = str(input("Enter Name: "))

#---------------------------------------STRINGS----------------------------------------

print("Hello Everyone \n and Hello World !!")  #gives next line 

#Concatenation:
str1 = "Hello"
str2 = "World !!"
print(str1 + " " + str2)  #prints Hello World !!

#Length of string:
length = len(str1) #5, even spaces are counted

#Indexing:
str3 = "Vinayak"
print(str3[0])  #prints 'V'
#By using Indexing, we cannot modify string --> gives error 

#Slicing: accessing parts of a string --> used in ML for cleaning data
print(str[0:4])  # prints 'Vina'
#ending index is not included in this slice

print(str[:4])  #str[0:4]
# python automatically fill gap by 0th index i.e first element

print(str[0:])  #str[0:len(str3)]
# python automatically fill gap by length of string i.e last element


#Slicing using Negative Indexing:
print(str[-1:-3]) #ending index is not included

#String Functions: 

#returns True if string ends with substring
name = name.endswith("er") 

#removes whitespaces from string(if any)
name = name.strip()

#capitalize 1st char of name
name = name.capitalize()

#replace 'all' old occurrences with new 
name = name.replace("o", "a") 

#finds given string into main string
name = name.find("vinayak")
#if it finds given string, then it returns index of its 1st occurrence

#counts no.of occurrences of substring in the main string
name = name.count("n")

#capitalize user's first & last name.
name = name.title()

#remove whitespace and capitalize first & last name using name. 
name = name.strip().title()

#split user's name into first and last name.
name = name.split(" ")
first, last = name.split(" ") #this assigns the 1st part to first and surname to last and can be printed by print(first/last).


#we can round number to certain digits when using float data type.
a = float(3.2)
b = float(1.2)
z = round(a+b) 
print(f"{z:.2f}") #2f at the end shows that we need answer upto 2 decimal values.
print(f"{z:,}") #this prints the number with a comma.
# f is used to tell python that this is a 'special string'




def hello():
    print("Hello !!")
#defining a function.

def hello(n):
    return n**2 #return statement is used to return a value to a function.
                #return is only used for functions.

# ls --> list
# mv --> move or rename
# rm --> remove file
# cp --> copy
# mkdir --> make directory 
# rmdir --> remove directory
# clear --> clears terminal  
# ..--> represents parent directory

#---------------------------------------CONDITIONALS--------------------------------------------------------------------------

# if
x = int(input("Enter 1st Number: "))
y = int(input("Enter 2nd Number: "))

if (x < y):
    print("x is less than y")

elif (x == y):                       
    print("x is equal to y")
                                   
else:                              
    print("x is greater than y")        

#using logical operator --> (or)

if (x < y or x > y):
    print("x is not equal to y")
else:
    print("x is equal to y")

# python allows to write conditions as ( 10 <= score <= 20 )

#Nesting --> conditonals inside conditionals or loop inside loop or mixed too 

def is_even(n):
    if n%2 ==0:
        return True  # Boolean.
    else:
        return False

# t of True is capital and f of False is capital.

def is_even(n):
    return True if n % 2 == 0 else False  # even more condensed.

grades = input("How much you scored ?: ")
match grades:                    # match is switch of C language.
    case "A": print("Excellent")
    case "B"|"B+"|"B-": print("Good")  # we can also add multiple cases by using (|) which is (or).
    case "C": print("Bad")
    case _ : print("Invalid")    # default case for switch.
 
# match in python doesn't need BREAK statements like in C language.   


#----------------------------------------LISTS------------------------------------------------------------------

# List --> arrays in C language shown by Square Brackets. 
''' It is a built-in data type which can even store different data types in 1 single list '''

animals = ["cat","dog","snake","ant"]    #stores only Strings
info = ["Hello Ji", 7, "8.9"]            #stores Strings, Int, Float

'''     Strings --> Immutable
        Lists --> Mutable
        Tuple --> Immutable     '''

print(animals[0])           #prints element at index 0.

list[0] = "Welcome Ji"      #replaces "Hello Ji" with "Welcome Ji" --> this shows Mutability

#Lists Methods:
list = [3,1,2]
'''a) Append --> adding something at the end of the list'''
list = list.append(4)   #list = [3,1,2,4]

'''b) Sort --> sorts elements in ascending order'''
list = list.sort        #sorted list = [1,2,3]

'''c) Sorting in Reverse --> sorts elements in descending order'''
list = list.sort(reverse = True)    #list = [3,2,1]

'''d) Reverse --> reverses the list (does not aarrange in descending order)'''
list = list.reverse             #list = [2,1,3]

'''e) Insert --> inserting a specific element at index'''
list = list.insert(1, 4)
#                 |    |
#               index  value

'''e) Remove --> removes 1st occurence of a specific element'''
list = [3,1,2,1]
list = list.remove(1)       #list = [3,2,1]
#so it removed 1st occurence of element '1'

'''f) Pop --> removes element from an index'''
list = [3,1,2]
list = list.pop(0)            #list = [1,2]
#removes element from 0th index

#----------------------------------------TUPLES------------------------------------------------------------------

'''It is a Built-in DATA TYPE that allows us to create Immutable sequences of values'''
# Uses Normal Braces --> ()

tuple = (7,12,2005)
print(type(tuple))          #gives <class 'tuple'>

print(tuple[1])         #12
print(tuple[1:2])       #12, 2005

tuple[2] = 2007     #now this is NOT allowed, this is what it means to be Immutable

#Tuple Methods:
'''a) Index --> ofc bro re-assignment is not allowed in tuples
                so it, returns index of 1st occurence of that element '''
tuple.index(2005)   #2
#             |
#           element

'''b) Count --> counts Total Occurence of a element'''
tup = (1,1,1,1,2)
tup.count(1)        #4


#NOTE: in all the methods never forget to use braces eg: list.reverse --> doesn't work ; list.reverse() --> this works

#------------------------------------DICTONARIES---------------------------- --------------------------
#It is a structure which is used to store data values in key:value pairs.
# They are Unordered, Mutable, but doesn't allow duplicate keys


avenger = {
    "name":"Tony Stark",                                                #str
    "age": 37,                                                          #int                                            
    "powers":["Genius", "Billonaire", "Playboy", "Phlantrophist"],      #tuple
    "friends": ("Steve Rogers", "Bruce Baner", "Vision", "Rodes"),      #list
    "total Percentage": 99.9,                                           #float
    "marks": {                                                          #dict(nested dictionary)
        "math": 100,
        "science": 100,
        "social science": 98 },                            
    "is_adult": True                                                    #bool
 }

#Duplicate keys are NOT allowed

#Mutablility: 
avenger["age"] = 40

#To access nested dict(dict in dict):
avenger["marks"]["science"]             #100

#Empty Dict:
null_dict = {}

print(animals)          #gives complete dict
animals["dog"]          #prints value with dog.

#or, use a loop to print.
for i in animals:          #we are referring to every key as i in animals.
    print(animals[i])

#dict with more info
animals ={
    {"name":"dog","class":"mammal","domestic":"YES"},
    {"name":"ant","class":"insect","domestic": None},
} #none is a keyword which shows nothing.


''' Dictionary Methods '''
# print only all keys:
avenger.keys()

# print only all values:
avenger.values()

# return all key:value pairs as Tuples:
avenger.items()

# to get value according to a key:
avenger['name']         #gives Name, but if mistyped --> gives Error
# 'Tony Stark'

avenger.get('name')     #also gives Name, but if mistyped --> gives None 
# 'Tony Stark'

#to update Dict with a new key:value pair:
avenger.update({'city':'New York'})

# avenger = {'name': 'Tony Stark', 
#  'age': 37, 
#  'powers': ['Genius', 'Billonaire', 'Playboy', 'Phlantrophist'], 
#  'friends': ('Steve Rogers', 'Bruce Baner', 'Vision', 'Rodes'), 
#  'total Percentage': 99.9, 
#  'marks': {'math': 100, 'science': 100, 'social science': 98}, 
#  'is_adult': True, 
''' 'city': 'New York'      '''
# }



#------------------------------------SETS---------------------------- --------------------------
'''It is a Data Type in python, used for collection of unordered items
   Condition: each element in set should be (a) Unique
                                            (b) Immutable '''

'''Set is Mutable, but its elements are Immutable i.e., we can Add/Remove elements in set 
    but we cannot change a element for other '''

'''Set being Unordered means final set can have different order of elements from 
    original '''

set = {1,2,3}       #written just like you would write in maths
print(type(set))    #<class 'set'>

set = {1,2,2,1}     # resolved to {1,2} 
#so repeated elements are stored only Once
len(set)            # 2  cuz --> duplicate value are Ignored

null_set = {}       #this is a empty dict
null_set = set()    #empty set

#sets can also store strings:
set1 = {1,2,3,'Hello'}

'''Set Methods'''
#add --> adds an element in set
set.add(4)          #{1,2,3,4}

#remove --> deletes element from set
set.remove(4)       #{1,2,3}

#clear --> empties the set i.e deletes all elements
set.clear()         #{} --> empty set

#pop --> removes a random element from set
set.pop()           #2
#{1,3,4} --> '2' got popped out 

#Union --> combines both set's value
set1 = {1,2,3}
set2 = {4,5,6}
set1.union(set2)        #{1,2,3,4,5,6}

#Intersection --> gives commmon value from sets 
set1 = {1,2,3}
set2 = {4,2,6}
set1.intersection(set2)  #{2}


 
#----------------------------------------LOOPS---------------------------------------------------------------------------------------------------
'''Used to repeat instructions'''
                        
'''While Loop: '''
i = 0
while(i < 3):                #(or)  while(True) --> infinite loop
    print("Hello")
    i = i+1                  #if condition is absent, program runs forever
#python doesn't use ++ (or) --

#Break --> terminates loop when encountered --> program exits loop 

#Continue --> skips current iteration and directly jumps to next iteration


'''For Loop: '''
list = [1,2,3]
for element in list:
    print(element)          #[1,2,3]

str = "Vinayak"
for char in str:
    print(char)             #v,i,n,a,y,a,k 
    
for i in range(0,100):   
    print("hello")          #prints 'hello' 100 times


'''For Loop with Else: '''
for element in list:
    print(element) 
else:                           #works when loop ends --> used to perform a task after loop ends
    print("Loop Ends !!")

#Range Func:
for i in range(11):         #0 is By Default, 11 is Excluded
    print(i)            

for i in range(0,11):       #0 is Included, but 11 is Excluded
    print(i)            

for i in range(0,11,2):       #0 is Included, 11 is Excluded, with 2 steps
    print(i)            


#Pass Statement --> null statement that does nothing, it is used as placeholder for future code 
for val in list: 
    pass



#---------------------------------------FUNCTION & RECURSION---------------------------------------------------------------------------------------------------
#Funcs --> block of code that performs a specific task

def sum(a, b):            #func defination
    print(a + b)

sum(2,3)                  #func call























#-----------------------------------------------------------------------------------------------------------------
                       #EXCEPTIONS
#Handling Errors

x = int(input("What is x?: "))

print("x is",x)
print(f"x is {x}")

#ValueError --> when we put str in int variable.
try:  #try block lets you test a code block for errors. 
    x = int(input("What is x?: "))
    print(f"x is {x}")

except ValueError: #except block lets you handle error.
    print("x is NOT integer!")   

 #NameError --> when we use variable / function that has NOT been defined.
try:
    x = int(input("What is x?: "))

except ValueError:
    print("x is NOT an integer")    

print(f"x is {x}")
#NameError shows when this print statement is written down,
#when string is put in x ValueError arises therefore, except is executed
#and try block was never successfully completed, so x has NO value and it does NOT exist in memory. 

# to solve this issue we can use --else--

try:                           #tu try kar 
    x = int(input("What is x?: "))
except ValueError:             #ValueError aye toh ye kar
    print("x is NOT an integer")    

else:                          #nhi toh ye kar 
    print(f"x is {x}")

#if we want to prompt user, again & again till they input correct.
while(True):
    try:
        x = int(input("What's x?: "))
        break     #break can be used here too, if we remove else.
    except ValueError:
        print("x is NOT an integer")
    else:
        break #(or) pass

print(f"x is {x}")    

#Pass --> used as a placeholder for future code.
#-----------------------------------------------------------------------------------------------------------------------------
                          #Debugging
# clicking on the red dot in vscode mark it as breakpoint.
#it makes various debugging options available.

#-----------------------------------------------------------------------------------------------------------------------------
                          #Libraries / Modules
                               # RANDOM

import random       #import allows to import lib.
# random is a lib which is used for probaility games.

                #choice function
coin = random.choice(["heads", "tails"])   #chooses either head  or tail.
print(coin)

# (or)
from random import choice     #we can choose specific functions from the lib.
coin = choice(["heads", "tails"])

                #randint function
from random import randint
number = randint(1,10)   #this chooses 1 int from 1 to 10.

                #shuffle function
from random import shuffle
cards = ["jack","queen","king"]
random.shuffle(cards)     # shuffles elements of a list.
for card in cards:        # for loop to get elements vertically.
    print(card)
                    
                              #STATISTICS
  # for average 
import statistics
print(statistics.mean([100,90]))

 # sys --> to incorporate command line arguments.
          #argv function
import sys
print("hello, my name is", sys.argv[1]) #argv takes input from keyboard, at 0 index it stores name of program and can store more if enclosed in " ".
# for more than 1 input in argv:
for arg in sys.argv[1:]:   # this introduces a range.
    print("hello, my name is",arg)

          #exit funciton
# break --> used in loops.
#exit --> exits the whole program.
import sys
if len(sys.argv) < 2:
    sys.exit("Too few arguments")   #sys.exit just prints the string and exits program.
elif len(sys.argv) > 2:
    sys.exit("Too many arguments")

print("hello, my name is", sys.argv[1])

                    
                         # PACKAGES --> 3rd party lib
#pip --> package manager
     #Cowsay
import cowsay
import sys
if len(sys.argv) == 2:
    cowsay.cow("hello,"+ sys.argv[1])                     
    cowsay.trex("hello,"+ sys.argv[1]) 

         #APIs (Applictaion Programming Interface)
# use 'requests lib' to make internet requests
#api uses JSON(Javascript Script Object Notation) file which is used as language agnostic format for exchanging data between computers.
# it means other programming languages can read a json file 
import requests
import sys
if len(sys.argv) != 2:
    sys.exit()

response=requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])
print(response.json)  
#requests itunes to send info about singer in json format
#we can format this josn file to get clearer view, by using json lib in python

       #JSON
import json #pass response.json to this and use json.dumps
print(json.dumps(response.json(), indent=2)) 

#we can make our own libraries as well.
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                                #STYLES

#PEP 8 --> proposal of how code should look like. Use pylint lib for it.
# or use pycodestyle which can fix style issues for us.
#more popular is BLACK. To initiate type black learn.py in terminal.

#------------------------------------------------------------------------------------------------------------------------------------------------------------
                                # Unit Tests --> to test units(functions) of our code.
#assert --> helps verify that a condition holds true during execution, if not AssertionError occurs 
assert 2*2 == 4
assert 3*3 == 9

#pytest --> 3rd party software to test code's unit which are funcitons.  pip install pytest. pytest learn.py
#to use it make a file with test_ eg: test_helloworld.py
#also we have to import the function from main file to test_file using:-- from main import hello(function)
#if we want pytest to show mercy on estimates we use :-- 
import pytest
assert is_even(a) == pytest.approx(149597870.691)
assert is_even(a) == pytest.approx(149597870.691, abs=0.1)
#abs limits the extent of variations in the value

#we can also raise errors when we want them specifically by:
# raise TypeError
# raise SyntaxError
# commented because it will make code below unreachable due to "raise"

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                                         # File I/O
name = [] #--> creates unlimited limit
for i in range(0,5):
    name.append(input("What's your name:"))

for elements in sorted(name):
    print("Hello",name)

                  #Write in a file
#open() --> to store 
file = open("learn.txt","w") #creates a file 
                             #w --> WRITE, if file don't exist yet, it will create it.
file.write(name) #tells to write name in file
file.close() #--> save file, so it doesn't vanishes when program is completed
#if we run (code learn.txt) in terminal we will see a text file with the name written, but whenever we write something new it replaces the previous one.

file = open("learn.txt","a") #a -->APPEND, it will add name without replacing them 1 below other
file.write(f"{name}\n") #--> stores names, 1 in each row

with open("name.txt","a") as file: #this is the format
    #file is the name of the varibale that is assigned the return value of open
    file.write(f"{name}\n")
#with --> automatically closes file, as not closing could delete stored data

                  #Read a file
with open("learn.txt","r") as file:
    lines = file.readlines()

for line in lines:          #for loop
    print("hello,",line, end="") # prints names in terminal with 1 in each row 
#if end is not written then the names are separated by 2 lines due to \n of print and due to file format from which names are extracted

                            #(OR)

with open("learn.txt","r") as file:
    for line in sorted(file):  #itertaes each line of the file
        print("hello,", line.rstrip())
# this shortens the above code also introducing rstrip which also fix the 2 line gap
    for line in sorted(file,reverse=True):# z to a
        print("hello") 

#learn.txt --> learn.csv;  csv--> comma separated values
#csv is used as convention to store multiple related info in the same file

with open("student.csv")as file:
    for line in file:
        name, house = line.rstrip().split(",")  #wherever "," appears slpit will split that line into 2
        print(f"{name}is in{house}")

#student[] --> unlimited list 
#student{} --> unlimited dictionary

#key --> identifier of associated value
def get_name(students):
    return students["name"]

for students in sorted(house, key = get_name, reverse=True):
    print(f"{students['name']} is in{students['house']}")

#lambda --> tells python, here comes a function with no name
#lambda is anonymous function
for students in sorted(house, key = lambda students: students["name"]):
        print(f"{students['name']} is in{students['house']}")

         #CSV
import csv
with open("learn.csv","r")as file:
    reader = csv.reader(file)  #reads csv file as list

    reader = csv.DictReader(file)  #reads csv file as dictionary, which takes care of the order and commas in string itself

name = input("Name: ")
home = input("House: ")
with open("1.csv","a") as file:
    writer = csv.writer(file)     # writes in csv file
    writer.writerow([name,home])  # writes in row in that csv file   
    # name and home in writerow defines rows

# if we don't want to care about rows and orders we will use dictionary again --> DictWriter
    writer = csv.DictWriter(file, fieldnames=["name","home"]) #fieldnames give dictwriter a hint about order in which the columns are when writting it out
    writer.writerow({"name":name, "home":home})
                    #column      #column

    #PIL (PILLOW) --> manipulates images
#making of a gif with endless loop
import sys
from PIL import Image

images = []

for arg in sys.argv[1:]:
    image = Image.open(arg)
    images.append(image)

images[0].save("costume.gif" save_all = True,append_images=(images[1],duration = 200,loop = 0 ))


from PIL import Image
def main():
    img = Image.open("hello.jpeg") # (OR) with Image.open("hello.jpeg")as img:   --> writting this will not require closing statement
    img.close()
    img.rotate(180) #rotates image by 180 degrees
    print(img.size)
    print(img.format) #--> jpeg
    img.save("hello.jpeg") #saves the image's modified version 

# image filters
from PIL import ImageFilter

with Image.open("hello.jpeg") as img:
    img = img.filter(ImageFilter.BLUR) #blurs image
    img = img.filter(ImageFilter.FIND_EDGES) #highlights edges in image(in object in image also)
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                                #Regular Expressions (REGEX)

#to validate if the given input is a email or not 
email = input("whats' your input?: ").strip()

if "@" in email and "." in email: #uses logical 'and'
    print("Valid") 
else:
    print("Invalid")

             #re.search
import re
email = input("whats' your input?: ").strip()

#re.search --> searches for given arguments in string 
if re.search("@",email):
    print("valid")
else:
    print("invalid")

#more powerful:
#  . --> represents a character (except newline)
#  + --> 1 or more repetitions
#  * --> 0(not persent) or more repetitions of something 
#  ? --> 0 or 1 repetition
# {m} --> 'm' no.of repetitions
# {m-n} --> 'm-n' no.of repetitions

if re.search(".*@.*",email): # (.*) means repetition(as many) of characters(any) on both left and right side of @ (OR) nothing because * also accepts 0
    print("valid")
else:
    print("invalid")

if re.search(".+@.+",email): #(.+) also means repetition(as many) of characters(any) on both left and right side of @ (OR) 1 repetition
    print("valid")
else:
    print("invalid")

#to ensure that the input email ends with (.com) we can use a backslash(\) otherwise python interprets it as (+.) which means add one or more repetitions after @ 
if re.search(r".+@.+\.com",email): #(\)separates + and .com
#so that python does not misinterpret (\), we add (r) which means raw string this tells python not to interpret (\) in usual way
    print("valid")
else:
    print("invalid")

#this code will return validate if we type say vinayak gaur ji@gmail.com -- which is incorrect
#so if we want to add start and end points we use:

# ^ --> start of string 
# $ --> end of string 
if re.search(r"^.+@.+\.com$",email):
    print("valid")
else:
    print("invalid")

#to make conditions more specific we have more expressions:
#[] --> set of characters that are allowed
#[^] --> any character, EXCEPT the character inside bracket
if re.search(r"^[^@] + @[^@] + \.com$",email):  #as any character is allowed except the character inside, we do not need (.) anymore because it represents any character
    print("valid")
else:
    print("invalid")
#[^@] on left and right of main @ means that strings on left and right of main @ should not have @

#to make even more specific for eg--> by allowing only like small case alphabets --> [a-z]
if re.search(r"^[a-z] + @[^@] + \.com$",email):  #as any character is allowed except the character inside, we do not need (.) anymore because it represents any character
    print("valid")
else:
    print("invalid")

#to make even more specific for eg--> by also allowing capital case alphabets --> [A-Z] & numbers --> [0-9] & symbols --> _(underscore)
#these should be written without gaps 
if re.search(r"^[a-zA-Z0-9_] + @[^@] + \.com$",email):
    print("valid")
else:
    print("invalid")
# these conditions can be pasted in place of [^@], to make it more narrow and strict

# these [a-zA-Z0-9_] are represented by (\w) (built-in)  
if re.search(r"^\w + @\w + \.com$",email):
    print("valid")
else:
    print("invalid")

#\d --> decimal digit 
#\D --> NOT a decimal digit 

#\s --> whitespace characters
#\S --> NOT a whitespace character

#\w --> word character... as well as the numbers and underscore
#\W --> NOT a word character

#to add more entries like .edu, .gov, .net, .org as well
#and also to add more specifications like \w & \s together we use:
  # A|B --> either A or B
  # () --> to group things together

if re.search(r"^ (\w|\s) + @\w + \.(com|edu|gov|net|org) $",email):
    print("valid")
else:
    print("invalid")

#re search also includes a 3rd argument = flags ; these are configurations 
#re.IGNORECASE --> upper & lower cases are ignored; so it becomes case insensitive
#re.MULTILINE --> when a paragraph is written in multiple lines it should match the beginning of every line 
#re.DOTALL --> recognise any character with new line

if re.search(r"^ (\w|\.) + @\w + \.(com|edu|gov|net|org) $",email, re.IGNORECASE):
    print("valid")
else:
    print("invalid")

# to put 2 choices for emails, either this or that we use ? --> 0 or 1 repetition
if re.search(r"^ (\w|\.) + @(\w+\.)?\w + \.(com|edu|gov|net|org) $",email):
    print("valid")
else:
    print("invalid")
# here (\w + \.) allows 2 dots(one of which belongs to .edu/gov/net/org/com) after @ and (\w) allows input of word character
# but (\w + \.)? \w --> tells re.search that either the things in bracket will repeat once or 0 times

# GAPS IN THE RE.SEARCH EXPRESSIONS(inside brackets) ARE WRONG 

#library for validating emails are also present on the internet

                #re.match
#similar to re.search except, we don't have to mark the beginning of regex to match the start of the string

              #re.fullmatch
#we don't need to mark the ending also



name = input("Enter name: ").strip()
if "," in name:      #works in cases where user didn't inputted as expected for eg: surname followed by name and a comma in between
    last, first = name.split(", "|",") #if comma is present in name as described in eg, this line splits it and overwrites it 
                                    
    name = f"{first} {last}" #pastes the pieces together in a variable
print(f"Hello, {name}")

# same problem with re:
import re
name = input("Enter name: ").strip()
matches = re.search(r"^(.+), ?(.+)$", name) #() --> capturing portion 
                                           #(?:) --> non-captring portion
                            # ? --> makes having a whitespace after comma in name optional so that now both inputs are allowed
if matches:  #if there is a format like matches then...
    last = matches.groups(1)   #group thing 1 that was captured from matches
    first = matches.groups(2)  #group thing 2 that was captured from matches
    name = f"{first}{last}"    
print(f"hello, {name}")
              
                        #(OR)
if matches := re.search(r"^(.+), ?(.+)$", name):  #:=(Walrus Operator) is used only when we want to assign from left to right and also want to ask a if or elif question on the same line
    name = matches.group(2) + " " + matches.group(1)
            # first name     #gap    #surname
print(f"hello,{name}")

#according to documentation numbering in groups starts from 1 by convention and not 0

#if we want to replace something with the other 
url = input("URL: ").strip()

username = url.replace("https://twitter.com/","") #this replaces the https://twitter.com/ part with just a blank
print(f"Usename is {username}")

#if we want to remove something before a specific character 
username = url.removeprefix("https://twitter.com") #now this removes https part also just like replace 

#similarly if we want to remove suffix 
username = url.removesuffix("https://twitter.com")
#also NO 2nd parameter is required in these 

#same problem with re
      #re.sub --> used for substitution
import re

url = input("URL:").strip()

username = re.sub(r"(^https?://)?(www\.)?twitter.com/", "", url)  #? shows that s and (www.) is optional so that user can input both https or http (or) url without www. and with it as well
                 #what to substitute             #by what  #in what
print(f"Username:{username}")
# (https://) is also made optional by using ? so user can type it or not type as well 
# \(backslash) in (www\.) ensures that python does not confuse (www.) with (www and a character)

#(www\.)? --> this makes (www.) optional
#(www\.|) --> this makes (www.) or gap 

#by using re.search
variable = re.search(r"^https://(www\.)?twitter\.com/(.+)$", url, re.IGNORECASE)
if variable:
    print(f"Username is: ", variable.group(2)) #prints things in group 2 ie (.+) which is username

#(OR)
#by using walrus operator
if variable := re.search(r"^https://(www\.)?twitter\.(?:com|org)/(.+)$", url, re.IGNORECASE):
    print(f"Username is: ", variable.group(2))
#(?:) in (com|org) tells python to make it non-capturing, so that now it cannot be included in group numbering 

#other re functions: #re.split --> via which we can split a string by mulltiple characters and not just commas 
                     #re.findall --> allows to search for multiple copies of same patterns in different places in a string

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                               #Object-Oriented Programming (OOPS)

                                        #TUPLE --> type of data which is collection of data like x,y,z but it is IMMUTABLE
def main():
    name, house = get_student()   # to pass 2 different parameters to the same function in the same line 
    print(f"{name} from {house}")

def get_student():
    name = input("Name: ")    #to define 2 different variables in a single function
    house = input("House: ")
    return (name, house)        #to get 2 or more returns in a single function
       #this returns a tuple


if __name__ == "__main__": #when we want to call main function from a different file to different file we use:
    main()

#Tuples are immutable ie they cannot be updated by the user in terminal
def main():
    name, house = get_student()  
    if name == "Padma":
        house = "Ravenclaw"       
    #now, if this program runs and the user inputs name as Padma but puts house as Gryffindor, python will show up a TypeError cuz tuple saved house with padma as ravenclaw.
    #thus showing that tuple is immutable and cannot be updated 
    print(f"{name} from {house}")

def get_student():
    name = input("Name: ")    
    house = input("House: ")
    return (name, house)   #represents a tuple  
    #return [name, house]  #represents a list

if __name__ == "__main__":
    main()

#() --> represents TUPLE => immutable; cannot be updated by user
#[] --> represents LISTS => mutable; can be updated by user 
#{} --> represents DICTIONARY => mutable

# whenever we access list or tuple or dictionary by indexing, we always use square-brackets []

#we can also use dictionary:
def get_student():
    student = {}             #empty dictionary 
    student["name"] = input("Name: ")
    student["house"] = input("House: ")
    return student 

#Class --> allows us to create our own data types and give them names 

class Student:         #by convention the 1st letter after class is Capital
      ...              #placeholder for future

def get_student():
    student = Student()    #creating an object of that class
    student.name = input("Name: ")
    student.house = input("House: ")
    return student

#we create objects/instances from classes
#Classes --> are mutable but we can make them immutable also
     #(OR)
def get_student():
    name = input("Name: ")
    house = input("House: ")
    student = Student(name, house)  #variable is assigned a class
    return student


#methods --> is a function inside a class, which behaves in a special way
#these functions allows us to determine behaviour in standard way
class Student:
    def __init__(self, name, house):  #parameter self gives access to object that was just created 
        self.name = name              #attribute aka instance variable 
        self.house = house

def get_student():
    name = input("Name: ")
    house = input("House: ")
    student = Student(name, house)  #this is constructor call --> construct a student object for us by using Student class as a templateso thta every student is structured the same  
    return student
#python will automatically call init method (function in class) and will automatically pass in a reference argument that represents the current object, that it just created in memory

#with class we have power to take more arguments(2 or more as much as we want), or list

#raise --> to make your own errors 
if not name:
    raise ValueError("Missing Name")   #value error will also show up text --> missing name 

if house not in ["Gryffindor", "Ravenclaw", "Slytherin"]:
    raise ValueError("Invalid house")

#we can catch errors using try and except statements 

#__str__ --> special method inside class, python calls this function when another function wants to see our object as a string
def __str__(self):
    return f"{self.name} from {self.house}"

def main():
    student = get_student()
    print(student) 

#emojis are put in "" cuz they are characters 

#to create personal methods --> by prefixing its name with double underscores (__)
def public_method(self):
        print("This is a public method.")
        self.__private_method()

def __private_method(self):
        print("This is a private method.")

#properties --> 
#decorators --> functions that modify functions of other functions

@property       #--> tells python that we are using a getter here
def house(self):      #Getter --> function for a class that gets some attribute
    return self.house 

@house.setter   #--> tells pyhton that we are using a setter here
def house(self, house): #Setter --> function for a class that sets some value 
    self.house = house
    print(name,"is in", random.choice(self.houses))  #this chooses one of them randomly also remember --> import random
#sign convention:  ._  (single underscore)--> don't touch this variable
#                  .__ (double underscore) --> really don't touch this variable

#int, str, list, dict, etc are also classes
#str.lower(), str.strip, list.append(x),etc are objects in these classes

#run print(type(50)) --> this prints exactly == <class 'int'>  
#run print(type({})) --> this prints exactly == <class 'dict'>  

#Class Methods:
class Hat:
    houses = ["Gryffindor","Hufflepuff","Ravenclaw","Slytherin"]

    @classmethod
    def sort(cls, name):       #cls is a keyword we use instead of class to avoid conflicts 
        print(name,"is in", random.choice(cls.houses)) 

    @classmethod
    def get(cls):              #get cls --> 
        name = input("Name: ")
        house = input("House: ")
        return cls(name, house)

Hat.sort("Harry")

#Inheritance

class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError("Missing Name")
        self.name = name

    ...

class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Missing Name")
        self.name = name
        self.house = house

    ...

class Professor:
    def __init__(self, name, subject):
        if not name:
            raise ValueError("Missing Name")
        self.name = name
        self.subject = subject

    ...
# class Professor(Wizard):
#     def __init__(self, name, subject):
#         self.subject = subject

    ...
#Operator Overloading --> when we assign more properties to operator 
#eg --> '+' represents addition but it is also used to concatenate strings
#Overloading is done by using __add__ and this can be used with any object

# Example of operator overloading inside a class
class Example:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):  # self is parameter on left of "+"
        if not isinstance(other, Example):
            return NotImplemented
        return Example(self.value + other.value)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                                       #Etc...
  #Set  --> sets in mathematics, prevents duplicate elements, implemented using func set()

list = ["Vinayak", "Harsh", "Aman", "Vinayak"] # list
list = list.set()   
list = {'Vinayak', 'Harsh', 'Aman'} 
#note: duplicate element got Removed, brackets becomes Curly, quotes becomes Single Quoted

# set also includes methods like --> add, remove, verify presence(using 'in' command --> "Vinayak" in list) --> returns True
# for something that is not present in set --> it returns False 

houses = set()
for student in students:
    houses.add(student["house"])

                    # Mathematical Opeartions on Set
# Intersection --> takes Common elements of a set --> &
list1 = {'Vinayak', 'Harsh', 'Aman'} 
list2 = {'Vinayak', 'Mani', 'Mayank'} 

list3 = list1 & list2  

# Union --> combines all elements of both sets (repeated ones are written once)--> .union
list1.union(list2)

# Subset --> checks if 1 set is subset of another set or not (True/False) --> .issubset
list1.issubset(list2)
#means list1 is subset of list2 or not




  #global --> tells python that this variable is global in program  
def demo():
    global balance
    balance = 0

#Type hints --> assigns data type when we need to mention it separately
def meow(n : int):  #this shows that n is specifically integer
    for _ in range(n):
        print("meow")
#mypy program checks for all type hints and then gives error and reason for its occurrence
# installed via pip install mypy

def meow(n: int) -> None:   #this annotation shows that this function returns None regardless of whether it has something inside it 
    for _ in range(n):
        print("meow")
# also mypy can detect it 
 

#doctstrings format --> helps to document your functions
#represented by either '''_''' (or) """_""" and define your property within it 

def moew(n: int) -> str:
    """"Meow n times
    
    :param n: Number of times to meow
    :type n: int
    :raise TypeError: If n is not an int 
    :return: A string of n meows, one per line
    :rtype: str    
    """
    return "meow\n" *n

#can also be used to find errors in our programs













