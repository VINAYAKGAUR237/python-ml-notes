
"""                               Statistics Fundamentals                           """

'''Statistics --> collection of facts,obseravtions,measurements used for analysis & interpretation to apply it for decision-making

It is study of data with ways to gather,review,analyze and arrive at meaningful conclusions

Importance:
        a) Data informed decision-making
        b) Understanding patterns and trends 
        c) Identify cuurent trends and predict future ones

Along with outputs that statistical analysis provide we can also get confidence intervals 
that helps us understands how certain we are about a conclusion


Common Terms Used In Statistics:
a) Population vs Sample
        >> Population is Complete pool from which Sample is drawn from it 
        >> Sample is a subset of population
We cannot perform statistical analysis on full pool of data --> costly, time-consuming
>> You can't Boil the Ocean
Therefore we use a subset(representative of population)--> sample

b) Measurement 
        >> it is a number/attribute that is calculated or measured for each member of the sample(height, weight, blood pressure,etc)

c) Parameter
        >> it is a characteristic of population(eg: population mean weight)

d) Statistics
        >> it is a characteristic of sample(eg: sample mean weight)

e) Distribution
        >> refers to how sample data is spread across range of values (frequency of diff values) 


        
Sampling Techniques:
a) Random Sampling --> every memeber of population has equal chance of being selected
b) Stratified Sampling --> divide population into subgroups(strata) and sample from each subgroup(stratum)
c) Snowball Sampling --> survey initial participants to respond and survey others they meet


Different Types of Statistics:
a) Descriptive  --> involves displaying, analyzing & describing data
                    (eg: avg BMI, max HorsePower, lowest school grade)
b) Inferential --> involves building conclusions(inferences) about population based on sample
                    (eg: Increase of bp causes Heart Attack)
c) Predictive  --> involves extracting info from data and using it to predict trends, behavior, patterns, relationships between attributes
                    (eg: predicting prices of goods when inflation is high, predicting demands of spare parts when a see a rise in car sales)

Description tells = 'what is'
Inferential tells = 'what likely is' based on a sample
Predictive tells = 'what might be' in the future 


Different Types of Data:
a) Categorical Data --> represents charateristics (eg: gender, blood type, country, etc)
b) Numerical Data --> represents data as measurement (eg: weight, height, speed, bp, etc)


Statistical Measures:
a) Measures of Central Tendency --> summary that describes the central position of the data 

    [if data is heavily skewed then these measures do not represent exact position]

These are: 3 M's --> Mean, Median, Mode

>> Mean --> sum of all data points divided by total count 
>> Median --> point in the centre after ranking data 
>> Mode --> most frequent point in data

'''
'''Mean: '''
#mean using pandas:
import pandas as pd
data = {
    'name':['Tony', 'Steve', 'Peter'],
    'age': [37, 35, 17],
    'score':[100, 75, 88],
    'city':['New York', 'Queens', 'Queens']
}
df = pd.DataFrame(data)
df['age'].mean(skpina=True)       #'skipna' --> skips missing values in data so that they are not included in mean


#mean using numpy:
import numpy as np
np.mean(df['age'])

#using numpy or pandas is recommended for best, fast performance


'''Median: '''
#using pandas:
df['age'].median()

#when no.of elements = Odd --> {1,2,4,5,6}            #median = 4
#when no.of elements = Even -->{1,2,4,5,6,8}            #median = (4+5)/2

'''Mode: '''
df['age'].mode()
#it is the only measure of central tendency that works with both categorical & numerical data

#if we dont have most freq value then pandas gives us a list about occurrences of item



'''b) Measures Of Dispersion --> mean may pose problem in describing data.
                It can be unreliable due to 2 reasons:
                        1) highly sensitive to outliers
                        2) may not be enough to decribe difference and full range of dataset
        
Measure of dispersion can help explain that:
1) Standard Deviation --> tells dispersion of data (spread of data) around mean
         eg: {1,4,6,8,9} --> more spread 
             {1,2,6,8,10} --> less spread
         
         Defined as 'Sum of Squares of Deviation around Mean Divided by No.of Observations
'''

#std using numpy:
data = np.array([1,2,3,6,7,8])
np.std(data)

#std using pandas: --> use describe() func
df.describe()


'''
2) Variance --> Square of Standard Deviation 

3) Range --> largest data pt - smallest data pt.
        Drawback : sensitive to outliers 

'''

df['age'].max()-df['age'].min()
#       |              |
#  largest value    smallest value

'''
4) Percentiles/Quartiles --> they are statistical concepts used to divide data into equal parts 
                             helping understand position of a single data point and distribution
                             of data 
        Percentiles divide data into 100 equal parts with each part representing a percentage of data 
        Common Percentiles: 
                        a) 25th percentile (Q1,P25) --> 25% of data falls below this 
                        a) 50th percentile (Q2,P50,Median) --> 50% of data falls below this 
                        a) 75th percentile (Q3,P75) --> 75% of data falls below this 
                        a) 90th percentile (P90) --> 90% of data falls below this 

        Quartiles: 4 quaters of the percentiles (Q1,Q2,Q3,Q4)
There are NO data points above 100 percentile
'''

#representation of percentile like a candle stick:
df.plot.box()
        #        ---                    
        #         |                   --> 75th percentile  
        #        ███                  --> 50th percentile
        #         |                   --> 25th percentile
        #        ---

#Box Area = InterQuartile Range

'''
5) Measure of Shape(skewness)
                Symmetric >> any distribution is called symmetric if it looks 
                           the same to the left and to the right of centre point
'''
#to get a distribution graph:
df['age'].hist()

'''Skewness --> measure of asymmetry/distortion of symmetric distribution
                it measures deviation of given distribution from a perfectly symmetric distribution 
                Having Outliers causes Skewness
                In ML, we avoid giving outliers to models but this leads to Data Loss'''

df['age'].skew()                #gives value for eg: -0.1511

'''a) Positive Skewness(Right skew) --> skewness > 0; distribution tail is stretched more towards right side 
   b) Negative Skewness(Left skew) --> skewness < 0; distribution tail is stretch more towards left
   c) Zero Skewness --> skewness ~ 0;  distribution is symmetric 


6) Measures Of Relationship:    
    >>  Previous measures falls under 'Univariate' analysis as it deals with one single variable/column/feature/array
        but measures of relationship deal with 'Multivariate' analysis (relationship between 2 or more variables)
        Covariance & Correlation only works for numerical variables

    a) Covariance --> gives direction of relationship if its Positive or Negative:
         >> Negative Covariance: if 'x' goes 'UP', then 'y' goes 'DOWN' (or vice versa)
         >> Positive Covariance: if 'x' goes 'UP', then 'y' goes 'UP' (or vice versa)

        eg: No.of patients in hospital goes UP, then beds available goes DOWN --> (-)
            Inflation goes UP, then prices of goods goes UP --> (+) 

    
    b) Correlation Coefficient --> most common measure cuz it gives both Direction(covariance) & Magnitude
                Its value ranges from -1 to +1:
                        i) corr = 0  --> no or very low relation (correlation)
                        ii) corr = close to +1 (> 0.6) --> 2 variables are highly positively correlated
                        iii) corr = close to -1 ( < 0.6) --> 2 variables are highly negatively correlated
 '''                    
data = {
    'income':[10000, 20000, 15000, 25000],
    'age':[25,34,27,37],
    'health_score':[95,60,90,57],
    'movies_watched':[7,4,4,9]
}

df = pd.DataFrame(data)
#    income  age  health_score  movies_watched
# 0   10000   25            95               7
# 1   20000   34            60               4
# 2   15000   27            90               4
# 3   25000   37            57               9

#we can use 'corr()' func to calculate correlation for all numeric values:
df.corr()               #gives correlation matrix 
#                   income       age  health_score  movies_watched
# income          1.000000  0.977525     -0.940153        0.316228
# age             0.977525  1.000000     -0.987000        0.335480
# health_score   -0.940153 -0.987000      1.000000       -0.233988
# movies_watched  0.316228  0.335480     -0.233988        1.000000

#age and health_score are negative correlation (closer to -1) --> age goes up, health_score goes down 
#age and income are positive correlation (closer to +1) --> age goes up, income goes up 



























































