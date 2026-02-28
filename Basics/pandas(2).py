                                # Intro To Pandas
#Pandas stands for Panel Datasets 
""" It is a Powerful, Flexible & easy to use open-source data analysis & manipulation tool 

    Uses:  1) Importing/Exporting Data
          2) Data Integration
          3) Data Aggregation and Manipulation
          4) Widely used in AIML for pre-processing structured data 

    Features:  1) Have powerful Data Structure
               2) Fast & Efficient Data Wrangling 
               3) Tools for Reading & Writing Data 
               4) Intelligent & Automated Data Alignment 
               5) High performance merging and joining of datasets 
           
    It has 2 main components:  1) Series  (1D)  --> 1D labeled array , supports multiple data types 
                               2) Dataframes  (2D) --> 2D labeled array, also supports multiple data types, input can be a series 
                                                                            or input can be another dataframe

            To install pandas: pip install pandas 
            Pandas req numpy therefore numpy should also be installed
            verify: import pandas as pd
     """
import pandas as pd
print(pd.__version__)         #gives version of pandas 


"""Pandas Series """
list = [1,2,3,4,5,6,7]
print(list)                   #[1, 2, 3, 4, 5, 6, 7]

series = pd.Series(list)
#OR
series = pd.Series([1,2,3,4,5,6,7])             # notice the Square Brackets inside 
print(series)
                              #     0    1
                              #     1    2
                              #     2    3
                              #     3    4
                              #     4    5
                              #     5    6
                              #     6    7
                              #   dtype: int64

#Rows becomes --> Columns
#Indexing & Data Type both are visible
#Accessing elements in Series:
series[2]                           #3

series[1:5]                         # range of indices 
# Upper range is included, Lower range is not included 

series2 = pd.Series([11,12,13], index =['x', 'y', 'z'])     # Customization of Indices
print(series2)
# x   11
# y   12
# z   13

#Accessing these: 
series2[1]              #12
series2['y']            #12
#both works 

#We can also convert Numpy Array --> Pandas Series
import numpy as np 

series = pd.Series(np.arange(2,30))       #so here 'np.arange' made a numpy array from 2 to 29 and then 'pd.series' made it a series

# 0      2
# 1      3
# 2      4
# 3      5
# 4      6
# 5      7
# 6      8
# 7      9
# 8     10
# 9     11
# 10    12
# 11    13
# 12    14
# 13    15
# 14    16
# 15    17
# 16    18
# 17    19
# 18    20
# 19    21
# 20    22
# 21    23
# 22    24
# 23    25
# 24    26
# 25    27
# 26    28
# 27    29
# dtype: int64



"""Pandas DataFrames """

'''Dataframe -> it is a 2D labeled structure (Table/Speadsheet) organised into Rows/Columns
                Labeling is done for Rows & Columns which allows for easier access and reading 
                This table can hold different data types even in same columns (like real world tables)
                NaN --> NOT A NUMBER (it represents Missing Values)
'''

#Convert Dictionary --> DataFrame
data = {
#     'key':'value'
      'name':["TonyStark", "SteveRogers", "PeterParker", "Thor"],
      'age':['37', '35', '17','150'],
      'HeroicName':["IronMan", "CaptainAmerica", "SpiderMan", "Thor"]
}

df = pd.DataFrame(data)
print(df)
#Output:
#           name  age      HeroicName
# 0    TonyStark   37         IronMan
# 1  SteveRogers   35  CaptainAmerica
# 2  PeterParker   17       SpiderMan
# 3         Thor  150            Thor

#this DataFrame stuff converts things into Labeled Table


#To get a specific Column of this table:
df['name']
# 0      TonyStark
# 1    SteveRogers
# 2    PeterParker
# 3           Thor
# Name: name, dtype: object

type(df['name'])        # <class 'pandas.core.series.Series'>     --> Series
type(df)                # <class 'pandas.core.frame.DataFrame'>   --> DataFrame

'''Therefore, we can say that DataFrame(Table) is a combination of Series(Columns)'''

''' Slicing & Dicing Data using loc() & iloc() function '''

#loc() --> location
#iloc() --> integer location  

#To get first 'Row':
df.loc[0]               # name          TonyStark
                        # age                  37
                        # HeroicName      IronMan
                        # Name: 0, dtype: object

#To get first Row & second Row
df.loc[[0,1]]           #           name age      HeroicName
                        # 0    TonyStark  37         IronMan
                        # 1  SteveRogers  35  CaptainAmerica

      #notice: their are Double Square Brackets inside

len(df)  #length = no.of Rows
df.ndim  #dimensions = 2
df.shape #shape = (4, 3) -> (No.of Rows, No.of Columns)

#Set Index --> set Row labels using 1 or more existing columns or arrays (of correct length)
df = pd.DataFrame({'month': [1, 4, 7, 10],
                     'year': [2012, 2014, 2013, 2014],
                     'sale': [55, 40, 84, 31]})

#    month  year  sale
# 0      1  2012    55
# 1      4  2014    40
# 2      7  2013    84
# 3     10  2014    31

df.set_index(np.arange(1, len(df)+1))         #this replaces index labeling with np array from 1 to (length+1) 
          
#    month  year  sale
# 1      1  2012    55
# 2      4  2014    40
# 3      7  2013    84
# 4     10  2014    31

#Here now index starts from 1, but if we print df again then, it reverts back to its original form where index starts from 0
#To make changes permanent we use 'inplace = True'
df.set_index(np.arange(1, len(df)+1), inplace=True)


df.dtypes               #gives Data Types of each Label
# name          object
# age           object
# HeroicName    object
# dtype: object


#Select all Rows & year Column only
df.loc[ : ,['year']]
#       |      |
#      rows  column


#Select all Rows & year,sales Column 
df.loc[ : ,['year', 'sale']]

#Apply condition on value of column
df.loc[df['sale']>40]

#Select first 2 rows & first 2 columns
df.loc[ :2, ['month', 'year']]
df.iloc[ :2, :2]                      #2 is not included only till 1

#Imagine having to print first 100 rows & columns in this case, iloc makes it easier 

df.iloc[-1, -1]  #grabs element from last

"""Use loc() when:
                  a) you need to access data by label
                  b) column position might change but you want to ensure that you are accessing correct column
                  c) when column name doesn't change
                  d) to increase code readibility
                  
   Use iloc() when:
                  a) you need to access data by index 
                  b) structure of df is stable(order of column)   """


#Making Dataframe from Lists
data_lists = [
    ['Tony', 'Steve', 'Peter'],
    [37, 35, 17],
    [100, 64, 92]
]

df = pd.DataFrame(data_lists)
#       0      1      2
# 0  Tony  Steve  Peter
# 1    37     35     17
# 2   100     64     92

""" To fix the Dataset:
                        a) Transpose the data to right form --> (Rows <--> Columns)
                        b) Define columns 
                        """

#Transpose:
df = df.T
#        0   1    2
# 0   Tony  37  100
# 1  Steve  35   64
# 2  Peter  17   92

#Define Columns:
df.columns = ['Name', 'Age', 'Grades']
#     Name Age Grades
# 0   Tony  37    100
# 1  Steve  35     64
# 2  Peter  17     92

#Pandas can apply all above functions in 1 line:
data_lists = [
    ['Tony', 'Steve', 'Peter'],
    [37, 35, 17],
    [100, 64, 92]
]
df = pd.DataFrame(data_lists).T.rename(columns = {0:'Name', 1:'Age', 2:'Grades'})
#                                                     |               
#                                 this shows that 0th column be labeled as 'Name'

#OR

df = pd.DataFrame(data_lists, index = ['Name', 'Age', 'Grades']).T


"""Methods of Iterating in Pandas"""

data_lists = {
   'Name':['Tony', 'Steve', 'Peter'],
    'Age':[37, 35, 17],
    'Grades':[100, 64, 92]
}
#     Name  Age  Grades
# 0   Tony   37     100
# 1  Steve   35      64
# 2  Peter   17      92

#print line : Tony is 37 years old and he got 100 marks 
print(f"{df.loc[0, 'Name']} is {df.loc[0, 'Age']} years old and he got {df.loc[0, 'Grades']} marks")
#              (Tony)                 (37)                                     (100)

#Now we can apply a loop and automate this using 'df.index' function:
for i in df.index:
            print(f"{df.loc[i, 'Name']} is {df.loc[i, 'Age']} years old and he got {df.loc[i, 'Grades']} marks")
      

#Update dataframe's values:
df['age'] = df['age'] + 10           #increase age by 10 years 
df['score'] = df['score'] / 100      #decimal value 

'''Using apply() & map() with pandas'''

'''apply() --> apply a condition or a func on a row/column'''

#apply() using Lambda func :
df['name'] = df['name'].apply(lambda x:x.upper())   #Uppercases all names
#     Name  Age  Grades
# 0   TONY   37     100
# 1  STEVE   35      64
# 2  PETER   17      92

#lambda func --> one-line func to perform quick, single-expression operation without needing def statement.
#we can also put if and else statement in lambda func too
df['age'] = df['age'].apply(lambda x: 'yes' if x > 35 else 'no')

#now in this func 'x' after 'lambda' is parameter and 'age' becomes argument

#apply() using Standard(Normal) func:
def func(x):
        if x > 35:
                return 'yes'
        else:
                return 'no'

df['age'] = df['age'].apply(func, axis = 1)
#axis = 1 --> applies to full column

#Drop a column --> to drop/delete a column 

df.drop(columns = 'Grades', inplace = True)  #note: it doesn't work when "df = df.drop(columns = 'Grades', inplace = True)"
#     Name  Age
# 0   TONY   37
# 1  STEVE   35
# 2  PETER   17


'''map() --> inserting a new column based on an existing column'''

df['Hero_name'] = df['Name'].map({'Tony': 'IronMan',
                                  'Steve': 'CaptainAmerica',
                                  'Peter': 'SpiderMan'})

#     Name  Age  Grades       Hero_name
# 0   Tony   37     100         IronMan
# 1  Steve   35      64  CaptainAmerica
# 2  Peter   17      92       SpiderMan


#replacing:
df['Hero_name'] = df['Hero_name'].str.replace('IronMan', 'Iron-Man')
#     Name  Age  Grades       Hero_name
# 0   Tony   37     100         Iron-Man
# 1  Steve   35      64  CaptainAmerica
# 2  Peter   17      92       SpiderMan


'''Sorting Data'''
df.sort_values(by='Age')                    #default: Ascending order 
#     Name  Age  Grades       hero_name
# 2  Peter   17      92       SpiderMan
# 1  Steve   35      64  CaptainAmerica
# 0   Tony   37     100         IronMan

#but it still doesn't change the original dataframe, or otherwise use 'inplace'

df.sort_values(by='Age', inplace = True)

#to get in Descending order:
df.sort_values(by='Age', inplace=True, ascending=False)
#     Name  Age  Grades       hero_name
# 0   Tony   37     100         IronMan
# 1  Steve   35      64  CaptainAmerica
# 2  Peter   17      92       SpiderMan


#NOTE: how index is shuffled in both ascending & descending order

#sort by 2 columns 1 ascending and 1 descending:
df.sort_values(by=['Age','Grades'], inplace=True, ascending=[True, False])

#so Age is sorted in Ascending order & Grades is sorted in Descending order

#Spotting Nulls:
import numpy as np
data = {
        'name': ['Tony', 'Steve', 'Peter', 'Bruce'],
        'age': [37, 35, np.nan, 37],                        #np.nan --> NAN : Not A Number
        'score': [99, 64, 87, 97],
        'city': ['New York', np.nan, 'Queens', np.nan]
}


df = pd.DataFrame(data)
#     name   age  score      city
# 0   Tony  37.0     99  New York
# 1  Steve  35.0     64       NaN
# 2  Peter   NaN     87    Queens
# 3  Bruce  37.0     97       NaN

'''Now to detect NULLS: '''
df.isna()
#     name    age  score   city
# 0  False  False  False  False
# 1  False  False  False   True
# 2  False   True  False  False
# 3  False  False  False   True

#Gives  Non-Nulls --> False  &   Nulls --> True
 
'''For large datasets we, Count NULLS in each column: '''
df.isna().sum()
# name     0
# age      1
# score    0
# city     2
# dtype: int64

#Shows that: name has 0 nulls, age has 2 , score has 0, city has 2

#To let pandas read a file use:
'''pd.read_file_type(file_name)'''




#--------------------------------------------- DATASET ----------------------------------------------------------------------
import pandas as pd
import numpy as np

#to read a file:
df = pd.read_csv('/home/vinayakgaur07/Downloads/Datasets/Lesson_04_Working_With_Pandas/Assisted_Practice_Dataset/HousePrices.csv')
#presents it in tabular form

#everything we are going to do on csv file is in memory and doesn't apply to original file

#get first 8 rows:
df.head(8)

#get last 8 columns:
df.tail(8)

#to randomly select 10 rows:
df.sample(10)

#(no.of rows, no.of columns)
df.shape                #(4600, 18)
df.shape[0]             #4600   --> Rows
df.shape[1]             #18     --> Columns


#to browse via data and get insights from data 
data.info()

# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 4600 entries, 0 to 4599
# Data columns (total 18 columns):
#  #   Column         Non-Null Count  Dtype  
# ---  ------         --------------  -----  
#  0   date           4600 non-null   object 
#  1   price          4600 non-null   float64
#  2   bedrooms       4600 non-null   float64
#  3   bathrooms      4600 non-null   float64
#  4   sqft_living    4600 non-null   int64  
#  5   sqft_lot       4600 non-null   int64  
#  6   floors         4600 non-null   float64
#  7   waterfront     4600 non-null   int64  
#  8   view           4600 non-null   int64  
#  9   condition      4600 non-null   int64  
#  10  sqft_above     4600 non-null   int64  
#  11  sqft_basement  4600 non-null   int64  
#  12  yr_built       4600 non-null   int64  
#  13  yr_renovated   4600 non-null   int64  
#  14  street         4600 non-null   object 
#  15  city           4600 non-null   object 
#  16  statezip       4600 non-null   object 
#  17  country        4600 non-null   object 
# dtypes: float64(4), int64(9), object(5)
# memory usage: 647.0+ KB                       --> rough estimate
# None

#to get actual memory consumption:
df.info(memory_usage='deep')

# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 4600 entries, 0 to 4599
# Data columns (total 18 columns):
#  #   Column         Non-Null Count  Dtype  
# ---  ------         --------------  -----  
#  0   date           4600 non-null   object 
#  1   price          4600 non-null   float64
#  2   bedrooms       4600 non-null   float64
#  3   bathrooms      4600 non-null   float64
#  4   sqft_living    4600 non-null   int64  
#  5   sqft_lot       4600 non-null   int64  
#  6   floors         4600 non-null   float64
#  7   waterfront     4600 non-null   int64  
#  8   view           4600 non-null   int64  
#  9   condition      4600 non-null   int64  
#  10  sqft_above     4600 non-null   int64  
#  11  sqft_basement  4600 non-null   int64  
#  12  yr_built       4600 non-null   int64  
#  13  yr_renovated   4600 non-null   int64  
#  14  street         4600 non-null   object 
#  15  city           4600 non-null   object 
#  16  statezip       4600 non-null   object 
#  17  country        4600 non-null   object 
# dtypes: float64(4), int64(9), object(5)
# memory usage: 1.8 MB                             --> actual 
# None


#select 2 columns with top 10 rows:
df[['bedrooms', 'country']].head(10)        #note 2 braces


#to get data types:
df.dtypes
# date              object
# price            float64
# bedrooms         float64
# bathrooms        float64
# sqft_living        int64
# sqft_lot           int64
# floors           float64
# waterfront         int64
# view               int64
# condition          int64
# sqft_above         int64
# sqft_basement      int64
# yr_built           int64
# yr_renovated       int64
# street            object
# city              object
# statezip          object
# country           object
# dtype: object

#to change data type of 'country' column to string:
df['country'] = df['country'].astype('string')
# date                     object
# price                   float64
# bedrooms                float64
# bathrooms               float64
# sqft_living               int64
# sqft_lot                  int64
# floors                  float64
# waterfront                int64
# view                      int64
# condition                 int64
# sqft_above                int64
# sqft_basement             int64
# yr_built                  int64
# yr_renovated              int64
# street                   object
# city                     object
# statezip                 object
# country          string[python]
# dtype: object

#to change data type of many values at once we use loop with astype func:
for col in df.select_dtypes(include=int).columns:
        df[col] = df[col].astype('int32')


#getting the sum of each column:
df.sum()
# date             2014-05-02 00:00:002014-05-02 00:00:002014-05-...
# price                                            2539029746.976785
# bedrooms                                                   15644.0
# bathrooms                                                  9939.75
# sqft_living                                                9840996
# sqft_lot                                                  68321574
# floors                                                      6955.5
# waterfront                                                      33
# view                                                          1107
# condition                                                    15878
# sqft_above                                                 8405421
# sqft_basement                                              1435575
# yr_built                                                   9065617
# yr_renovated                                               3719598
# street           18810 Densmore Ave N709 W Blaine St26206-26214...
# city             ShorelineSeattleKentBellevueRedmondSeattleRedm...
# statezip         WA 98133WA 98119WA 98042WA 98008WA 98052WA 981...
# country          USAUSAUSAUSAUSAUSAUSAUSAUSAUSAUSAUSAUSAUSAUSAU...
# dtype: object

#now to avoid this unusal thing we use:
df.sum(numeric_only=True)                   # -->gives sum for only number values 

# price            2.539030e+09
# bedrooms         1.564400e+04
# bathrooms        9.939750e+03
# sqft_living      9.840996e+06
# sqft_lot         6.832157e+07
# floors           6.955500e+03
# waterfront       3.300000e+01
# view             1.107000e+03
# condition        1.587800e+04
# sqft_above       8.405421e+06
# sqft_basement    1.435575e+06
# yr_built         9.065617e+06
# yr_renovated     3.719598e+06
# dtype: float64


#to get list of dataframe columns:
df.columns                          #note that this is without braces

# Index(['date', 'price', 'bedrooms', 'bathrooms', 'sqft_living', 'sqft_lot',
#        'floors', 'waterfront', 'view', 'condition', 'sqft_above',
#        'sqft_basement', 'yr_built', 'yr_renovated', 'street', 'city',
#        'statezip', 'country'],
#       dtype='object')

#now to replace something with other in column header:
df.columns = df.columns.str.replace(' ', '_')           #replaces space ' ' with underscore '_'

# Index(['date', 'price', 'bedrooms', 'bathrooms', 'sqft_living', 'sqft_lot',
#        'floors', 'waterfront', 'view', 'condition', 'sqft_above',
#        'sqft_basement', 'yr_built', 'yr_renovated', 'street', 'city',
#        'statezip', 'country'],
#       dtype='object')

#to remove leading or tailing spaces:
df.columns = df.columns.str.strip()     

#similarly:
df.columns = df.columns.str.upper()  #--> more str methods in recommendations

#similarly if we want to apply on a specific 1 column:
df['country']           #usa
df['country'].str.replace('USA', 'INDIA')

#Get Average of a column:
df['price'].mean()                  #551962.9884732141

#Get Average of whole data(column-wise average):
df.mean(numeric_only=True)
# price            551962.988473
# bedrooms              3.400870
# bathrooms             2.160815
# sqft_living        2139.346957
# sqft_lot          14852.516087
# floors                1.512065
# waterfront            0.007174
# view                  0.240652
# condition             3.451739
# sqft_above         1827.265435
# sqft_basement       312.081522
# yr_built           1970.786304
# yr_renovated        808.608261
# dtype: float64


#to get a statistical report(like mean, std, 25%,50%,75%, etc):
df.describe()
#               price     bedrooms    bathrooms  ...  sqft_basement     yr_built  yr_renovated
# count  4.600000e+03  4600.000000  4600.000000  ...    4600.000000  4600.000000   4600.000000
# mean   5.519630e+05     3.400870     2.160815  ...     312.081522  1970.786304    808.608261
# std    5.638347e+05     0.908848     0.783781  ...     464.137228    29.731848    979.414536
# min    0.000000e+00     0.000000     0.000000  ...       0.000000  1900.000000      0.000000
# 25%    3.228750e+05     3.000000     1.750000  ...       0.000000  1951.000000      0.000000
# 50%    4.609435e+05     3.000000     2.250000  ...       0.000000  1976.000000      0.000000
# 75%    6.549625e+05     4.000000     2.500000  ...     610.000000  1997.000000   1999.000000
# max    2.659000e+07     9.000000     8.000000  ...    4820.000000  2014.000000   2014.000000


'''this gives count --> no.of items
               mean --> avg
               std --> standard deviation
               min --> minimum value of each column
               max --> maximum value of each column
        percentiles --> 1st quater(25%), 2nd quater(50%), 3rd quater(75%)'''


#Build a new column, that gives avg of each row :
df['avg price'] = df.mean(numeric_only=True, axis=1)
#                                               |
#                                            column
df.head(3)
#                   date      price  bedrooms  ...  statezip  country      avg price
# 0  2014-05-02 00:00:00   313000.0       3.0  ...  WA 98133      USA   25197.000000
# 1  2014-05-02 00:00:00  2384000.0       5.0  ...  WA 98119      USA  184791.500000
# 2  2014-05-02 00:00:00   342000.0       3.0  ...  WA 98042      USA   27675.615385



#Build a new column, that gives avg of specific rows:
df['price'] = df[['without tax', 'with tax']].mean(axis = 1)        #--> gives avg of 2 columns into 1 column(price)
#using 'axis = 1' makes it Horizontal(Row) calculation

#logic of using 2 braces here is, that we are passing list of columns to data frame


#all things we done above are in memory and not in original csv file
#so, to save everything we have done --> save it in a file
df.to_csv('HousePrices.csv')

#this saves the new file into same folder as your previous data file


'''get top 10 houses that have prices < 5.5 lakhs: '''
df[df['price']<550000]                  #gives elements that are within cond


df[df['price']<550000].head(10)         #gives only 10 elements that are within cond

#to get sorted as well:
df[df['price']<550000].head(10).sort_values(by='prices')


#put in another cond with existing cond:
df[(df['price']<550000)&(df['price']>250000)]

'''select columns based on specific data type:'''
#select only numeric data:
df.int = df.select_dtypes(include='int')
df.int.head(3)

#exclude numeric data:
df.int = df.select_dtypes(exclude='int')
df.int.head(3)



'''                            Data Aggregation & Plotting                            '''
#find avg of prices:
df['price'].mean()

#finding Avg Of Prices using City as criteria:
df.groupby(['city'])[['price']].mean()
#OR
df[['city', 'price']].groupby('city').mean().round(2).head(3)
                         
# city                  price      
# Algona              207288.00
# Auburn              299340.44
# Beaux Arts Village  745000.00
# Bellevue            847180.66


#to convert data into visual(graph) --> use plot()
df[['city', 'price']].groupby('city').mean().round(2).head(3).plot(kind='bar')

#for this Matplotlib is req

#to get lowest price of house:
df[['city', 'price']].groupby('city').min()   #--> gives minimum value of each column

#                        price
# city                        
# Algona              100000.0
# Auburn                   0.0
# Beaux Arts Village  745000.0
# Bellevue                 0.0
# Black Diamond            0.0

'''Aggregation Function'''
#used to summarize data by applying one or more functions(mean, sum, min, max, count, etc) to columns
#these are most of the time used with groupby() func

df1 = pd.DataFrame({
    'A': [1, 2, 3, 4],
    'B': [10, 20, 30, 40]
})

df1.agg(['sum', 'mean'])
#then it makes a table with sum and mean of columns

#          A     B
# sum      10   100
# mean     2.5  25.0


df1.agg({'A': 'mean', 'B': 'sum'})
# A     2.5                     --> A = mean
# B   100.0                     --> B = sum
# dtype: float64

'''some more examples for usage of agg func:'''

#total(sum) of visits by gender 
df.groupby('gender').agg({'visits': 'sum'})


#avg income by health:
df.groupby('health').agg({'income':'mean'})


#avg visits by region:
df.groupby('region').agg({'visits':'mean'})




#value_count func:
df['price'].value_counts()      #It counts how many times each unique value appears in that column.

# 0.0          49               
# 300000.0     42               --> this price appeared 42 times
# 400000.0     31               --> this price appeared 31 times
# 440000.0     29               --> this price appeared 29 times and so on...
# 450000.0     29
#              ..               (truncation)
# 684680.0      1
# 609900.0      1
# 1635000.0     1
# 1339000.0     1
# 220600.0      1
# Name: count, Length: 1741, dtype: int64

#to get percentages:
df['price'].value_count(normalize=True)

# 0.0          0.01
# 300000.0     0.01
# 400000.0     0.01
# 440000.0     0.01
# 450000.0     0.01
#              ... 
# 684680.0     0.00
# 609900.0     0.00
# 1635000.0    0.00
# 1339000.0    0.00
# 220600.0     0.00
# Name: proportion, Length: 1741, dtype: float64


#to get data into bucket form:
df.value_counts(bins = 10)
# (45722.6, 101570.2]       501             --> 501 values range from 45722.6 to 101570.2 
# (101570.2, 157417.8]       64
# (157417.8, 213265.4]       17             --> 17 values range from 157417.8 to 213265.4
# (213265.4, 269113.0]        6
# (380808.2, 436655.8]        2


#Cut() func: --> cuts data into cut-points as specified in bins and classify them into bins
bins = [0, 50, 65, 80, 90, 100]
a = df['in_range'] = pd.cut((df['age']*10), bins)    #note: pd.cut and not df.cut
print(a.sample(10))
# 2227    (65, 80]
# 1154    (65, 80]
# 4362    (80, 90]
# 4162    (65, 80]
# 25      (65, 80]
# 395     (65, 80]
# 3110    (80, 90]
# 3503    (65, 80]
# 1964    (65, 80]
# 1693    (65, 80]



'''pivot_table() func:  this func helps us to create a customized spreadsheet style table
                        by specificing index to be used, column names, values inside table
                        and aggregation funcs to be used  '''

df.pivot_table(index='health', columns='gender', values='hospital', aggfunc=['sum','mean'])
#              sum           mean          
# gender    female male    female      male
# health                                   
# average      509  378  0.243192  0.266949
# excellent     11   23  0.056995  0.153333
# poor         231  152  0.675439  0.716981


'''Data Dictionary --> it is a simple table which is used to understand the meaning of columns and rows name
                        if they are abbreviated 
                         
also termed as Metadata --> info about the table '''



#Using Crosstab() func: --> it gives us no.of occurrences when 2 categories match
# works for 2 categorical columns

pd.crosstab(index = df['health'], columns = df['insurance'])          #note: pd.crosstab() not df.crosstab() 
# insurance   no   yes
# health              
# average    721  2788
# excellent   60   283
# poor       204   350


#scatter plot:
df.plot(kind = 'scatter')
#or to specify both 'x' & 'y' in the scatter plot
df.plot.scatter(x=df['income'], y=df['age'])

'''for both of these Matplotlib is req'''

#---------------------------------------------------------------------------------------------------------------------------------------------

'''                                  DATES IN PANDAS                          '''

'''Pandas can process dates during import or after import 
   It provides 2 primary data types to deal with date & time: 
                a) 'datetime64[ns]' --> represents a specific moment in time in nanosecond precision
                b) 'timedelta64[ns]' --> represents a duration, such as time difference between 2 dates '''

#Basic Concepts:
#Creating Date Range:
date_range = pd.date_range('12-7-2005', '10-26-2025')
#US Format --> month/day/year
# DatetimeIndex(['2005-12-07', '2005-12-08', '2005-12-09', '2005-12-10',
#                '2005-12-11', '2005-12-12', '2005-12-13', '2005-12-14',
#                '2005-12-15', '2005-12-16',
#                ...
#                '2025-10-17', '2025-10-18', '2025-10-19', '2025-10-20',
#                '2025-10-21', '2025-10-22', '2025-10-23', '2025-10-24',
#                '2025-10-25', '2025-10-26'],
#               dtype='datetime64[ns]', length=7264, freq='D')

# (default freq='D' --> day)

#we can adjust start, end, periods, frequency (week, day, hours)


# Parsing Dates:
#We can specify date format(dd/mm/yyyy), utc, origin of unix based format, errors('ignore', 'raise', 'coerce') tell pandas what to do in case of bad date format occurrence, etc

dates= ['2025-10-21', '2025-10-22', '2025-10-23', '2025-10-24', '2025-10-25', '2025-10-26']
pd.to_datetime(dates)      #default; without format

# DatetimeIndex(['2025-10-21', '2025-10-22', '2025-10-23', '2025-10-24',
#                '2025-10-25', '2025-10-26'],
#               dtype='datetime64[ns]', freq=None)


#to clear format to pandas (so that it doesn't have to guess format):
pd.to_datetime(dates, format='%Y/%m/%d')

'''Format --> should match the format of dates given:
                | Code | Meaning                | Example |
                | ---- | ---------------------- | ------- |
                | `%Y` | 4-digit year           | 2025    |
                | `%y` | 2-digit year           | 25      |
                | `%m` | Month (01-12)          | 10      |
                | `%b` | Abbreviated month name | Oct     |
                | `%B` | Full month name        | October |
                | `%d` | Day of month (01-31)   | 26      |
                | `%H` | Hour (00-23)-> 24 hr   | 15      |
                | `%I` | Hour (01-12)-> 12 hr   | 03      |
                | `%p` | AM/PM                  | PM      |
                | `%M` | Minute                 | 45      |
                | `%S` | Second                 | 09      |
                | `%f` | Microsecond            | 123456  |
                | `%z` | UTC offset             | +0000   |
                | `%Z` | Timezone               | UTC     |
                | `%a` | Weekday short name     | Sun     |
                | `%A` | Weekday full name      | Sunday  |
                
Formatting increases speed of program cuz now pandas wont have to guess format by itself
and also mistakes reduces when ambiguous date comes(3/8/2025) where pandas would have to guess


Error Handling in formats: using 'Raise', 'Coerce', 'Ignore' 

Raise:  default; when we don't specify error '''
pd.to_datetime(dates)           

'''Coerce: ignore invalid dates and turn them into NaT (Not a Time) type'''
pd.to_datetime(dates, format="%Y-%m-%d", errors='coerce')

'''Ignore: leaves date untouched, if parsing fails , does NO conversion to NaT'''
pd.to_datetime(dates, format="%Y-%m-%d", errors='ignore')


#to convert into preferred format:
date_list = pd.to_datetime(dates, format='%Y/%m/%d')
date_list.strftime('%d/%m/%Y')          #this gives dd/mm/yyyy format
#but after this we cannot run date operations


#DATE ARITHMETICS --> performed using 'timedelta        '

dates= ['2025-10-21', '2025-10-22', '2025-10-23', '2025-10-24', 
        '2025-10-25', '2025-10-26']

#Add/Subtract '3 days' to each date:
dates = dates + pd.Timedelta(days = 3) 
#                               |
#                           parameter
#       (days, hours, minutes, secs, millisecs, microsecs, weeks ,etc)

#with date vs date operations, no need to use 'timedelta' as long as both have same datetime format

date1 = pd.to_datetime('2024-10-21')
date2 = pd.to_datetime('2025-10-26')

diff = date2 - date1                 # 370 days 00:00:00


'''     Date Funcs:     '''
#Extracting Date Componenets(year, month, day, etc):

date1 = pd.to_datetime('2024-10-21')

my_year = date1.year            #2024
my_month = date1.month          #10
my_day = date1.day              #21

#These becomes useful in feature engineering o extract date parts and not using full dates

#Finding Day Of The Week:
date1 = pd.to_datetime('2024-10-21')
day_of_week = date1.day_of_week              # 0 --> 0th day of week 

#Name of the day of the week:
date1 = pd.to_datetime('2024-10-21')
day_of_week = date1.strftime('%A')           #Monday


#----------------------------------------- DATASET ---------------------------------------------------

df = pd.read_csv('/home/vinayakgaur07/Downloads/mar1and2_1749198872443/Mar 1 and 2/Drug_Sales (1).csv')

'''Now, there are 2 methods to parse dates in the data:
            a) after import --> after importing use 'to_datetime()'
            b) during import --> add 'parse_dates' in 'read.csv()'
'''


#Method 1 --> parsing 'after import':
df['Date'] = pd.to_datetime(df['Date'])



#Method 2 --> parsing 'during import':
df = pd.read_csv('/home/vinayakgaur07/Downloads'
'/mar1and2_1749198872443/Mar 1 and 2/Drug_Sales (1).csv', parse_dates=['Date'])
#                                                               |
#                                                      parse_dates attribute


'''Feature Extraction:
                after we convert the date column to 'datetime' format, only then we are 
                able to run different date operations and able to extract date parts

It is a good practice to define new columns and insert them next to date format for 
readability, using 'insert()' func
'''

#insert() func:

df.insert(1, 'Year', df['Date'].dt.year)
#         |      |         |
#   (index)  (new column)  (column from which we extract)

df.insert(2, 'Month', df['Date'].dt.month)
df.insert(3, 'Day', df['Date'].dt.day)

#       Date    Year   Month  Day  ...  Drug5_Sales  Drug6_Sales  Drug7_Sales  Drug8_Sales
# 0 2019-09-01  2019      9    1  ...       4510.0      10000.0       2250.0       3600.0
# 1 2019-09-02  2019      9    2  ...       3850.0          0.0        450.0       8100.0
# 2 2019-09-03  2019      9    3  ...       4400.0      30000.0        450.0       1800.0
# 3 2019-09-04  2019      9    4  ...       3850.0          0.0       1350.0       2700.0
# 4 2019-09-05  2019      9    5  ...        550.0          0.0        450.0       7200.0


#using 'strftime()' func to extract other date parts like name of day(sun, mon,etc)
df.insert(3, 'Day Name', df['Date'].dt.strftime('%A'))

#         Date  Year  Month   Day Name  ...  Drug5_Sales  Drug6_Sales  Drug7_Sales  Drug8_Sales
# 0 2019-09-01  2019      9     Sunday  ...       4510.0      10000.0       2250.0       3600.0
# 1 2019-09-02  2019      9     Monday  ...       3850.0          0.0        450.0       8100.0
# 2 2019-09-03  2019      9    Tuesday  ...       4400.0      30000.0        450.0       1800.0
# 3 2019-09-04  2019      9  Wednesday  ...       3850.0          0.0       1350.0       2700.0
# 4 2019-09-05  2019      9   Thursday  ...        550.0          0.0        450.0       7200.0


#lets say in a big table we cant count the indexes and we want to insert after a specific column:
#then we can use get_loc() func to get index of any column:
df.columns.get_loc('Date')+1            #1

#'+1' shows that we aren't counting from 0


'''Date Filtering --> extracting dates from 1 date to another date range 
        For this we use Conditions using &, |, etc :'''

date_filter = (df['Date']>'2019-09-02')&(df['Date']<'2019-09-20')
print(df[date_filter])           #note: see how we didnt used quotes for date_filter cuz it is not a dataframe column

#          Date  Drug1  Drug2  Drug3  ...  Drug5_Sales  Drug6_Sales  Drug7_Sales  Drug8_Sales
# 2  2019-09-03   9.36  2.350   3.10  ...       4400.0      30000.0        450.0       1800.0
# 3  2019-09-04   2.00  0.373   2.15  ...       3850.0          0.0       1350.0       2700.0
# 4  2019-09-05   7.00  9.530   2.00  ...        550.0          0.0        450.0       7200.0
# 5  2019-09-06   1.68  2.670   1.00  ...       3850.0          0.0          0.0       1350.0
# 6  2019-09-07   8.33  3.670   2.00  ...       7700.0      30000.0       2700.0       1800.0
# 7  2019-09-08   7.01  6.087   3.00  ...       3850.0          0.0       1350.0       2700.0
# 8  2019-09-09   1.18  2.124   3.00  ...       2200.0      30000.0       2250.0       1800.0
# 9  2019-09-10   8.66  6.680   4.20  ...       9350.0          0.0        450.0        900.0
# 10 2019-09-11   2.67  5.076   3.00  ...       2750.0          0.0       2250.0       2250.0
# 11 2019-09-12   2.33  1.340   2.00  ...       6160.0          0.0       4500.0       3600.0
# 12 2019-09-13   6.34  3.350   2.00  ...       6600.0      20000.0       2250.0       4500.0
# 13 2019-09-14   8.99  6.397   3.45  ...       6600.0          0.0        900.0       9000.0
# 14 2019-09-15   5.34  6.010   2.00  ...       3300.0          0.0        900.0       5400.0
# 15 2019-09-16   9.33  2.316   3.00  ...       2750.0      10000.0          0.0       1800.0
# 16 2019-09-17   4.50  3.007   6.50  ...       4510.0          0.0       2700.0       1800.0
# 17 2019-09-18   6.33  4.330   7.00  ...       2200.0          0.0        900.0       1800.0
# 18 2019-09-19   7.33  3.340   3.00  ...       2750.0      20000.0       1350.0       3600.0


'''Aggregating Dates'''
#if we have already have date parts extracted, use those columns(eg: Year, Month)
#if we dont have date parts we can use, 'resample()' func
 

#Example-1: Get total sales by 'Day Name' for 'Drug1'

df.groupby('Day Name').agg({'Drug1':'sum'})
#            Drug1
# Day Name        
# Friday     18.02
# Monday     23.18
# Saturday   35.00
# Sunday     21.19
# Thursday   22.16
# Tuesday    24.52
# Wednesday  17.00


#Example-2: before using 'resample()' func we need to convert date column into an index:

df.set_index('Date', drop=True, inplace=True)     #this sets 'Date' as index
print(df.head())
#'drop=True'--> removes date as column and convert it to index

#             Drug1  Drug2  Drug3   Drug4  ...  Drug5_Sales  Drug6_Sales  Drug7_Sales  Drug8_Sales
# Date                                     ...                                                    
# 2019-09-01   2.00  4.360   5.00  17.000  ...       4510.0      10000.0       2250.0       3600.0
# 2019-09-02   5.33  2.087   2.50  18.000  ...       3850.0          0.0        450.0       8100.0
# 2019-09-03   9.36  2.350   3.10  12.125  ...       4400.0      30000.0        450.0       1800.0
# 2019-09-04   2.00  0.373   2.15  29.230  ...       3850.0          0.0       1350.0       2700.0
# 2019-09-05   7.00  9.530   2.00  14.000  ...        550.0          0.0        450.0       7200.0



#now as the date column is converted to index we can use resample() --> groups date (by years, months, weeks, days, 3days)   
#below is sum of all numeric values by week:

#resampling by week --> resample('W')
week_sum = df.drop(columns=['Year', 'Month', 'Day Name']).resample('W')
#so year, month, day name are dropped and indexes are grouped in weeks


#Compare 2 columns:
#eg: compare drug1 sales vs drug2 sales(with help of graph):
week_sum[['Drug1', 'Drug2']].plot(kind='bar')














































