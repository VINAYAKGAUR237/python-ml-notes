'''                 Advanced Statistics Using Hypothesis Testing            

Hypothesis --> statement that proposes a possible explanation for an observed 
                phenomenon or relationship, which scientists/mathematicians can test
                via investigation or statistics analysis

    Cycle of Hypothesis: 
    Careful experimentation --> Correct Sampling --> Data Collection --> Analysis --> Repitition for Reproductibility   

A good hypothesis must explicitily state the dependent and independent variable, it should also be testibile and have reproducibility
and be based on authentic research and sample collection (good data from population)

Also, state NULL and alternative hypothesis

    Hypothesis have 2 main components: a) Dependent Variable
                                       b) Independent Variable 

    Eg: if we dont clean fish tank every 3 months, then fishes will not survive 
        independent variable: "if we dont clean fish tank every 3 months"
        dependent variable: "then fishes will not survive"


        
Hypothesis Testing --> its a statistical method used to determine whether there is enough evidence 
                        in a sample of data to infer whether a certain condition holds true or not 
To do this we learn concepts like:
            a) NULL Hypothesis(H0): statement of no effect or no differences
                                    eg: no relation between age and income 

            b) Alternative Hypothesis(Ha or H1): statement that we want to prove, where there is 
                                                statisticially significant evidence 
                This is what you want to prove to be correct based on your idea or observation
                eg: there exist a relation between age and income
If we don't have sufficient evidence then we fail to reject null hypothesis --> i.e we fail to reject the idea that there is no relation

            c) Significance/Critical Level (alpha): it is probability of rejecting null hypothesis

            In industry, we use Critical Level = 5%(0.05) (sometimes 1% for strict evaluation)
                5% not chance vs 95% yes chance
                      |               |
               null hypothesis   alternate hypothesis  

            d) P-value: probability of a statement from a sample being true 


Once we have components above we can do hypothesis evaluation by using foll steps:
1. define statement of hypothesis
2. format statement into H0 & H1 
3. then choose appropriate statistical test:
        - t test
        - z test
        - chi square test 
        - ANOVA
        - Others: MANOVA, Mann-Whitney U Test, Kruskal-Wallis Test
4. set an alpha value(generally = 5%) --> this can be set up by us
5. calculate p-value using statistical funcs using python and given dataset
6. based on p-value and alpha, we also use u(mew) in evaluation which represents sample average:
            if p-value is greater than alpha then --> we dont reject null hypothesis --> we accept null hypothesis
            if p-value is less than alpha then --> we do reject null hypothesis --> we accept alternative hypothesis


T-Test:
Used when:
        a)For comparing 2 segments of sample using 1 numeric measure(eg: measuring temp)
        b)When sample size is very small(<=30) -OR- population's standard deviation is unknown

Types of T-test:
a)Independent Sample T-Test : evaluating if 2 independent, unrelated groups are same or not 
                                eg: grp of people that eat banana have high potassium vs grp of people that dont eat banana
                                For grp 1 vs grp 2 :         #NOTE : u = average; u1 = avg of grp1; u2 = avg of grp2
                                - for null hypothesis(h0) --> u1 = u2           => there's no difference
                                - for alternative hypothesis(h1) --> u1 != u2   => bananas are causing an impact

b)Paired Sample T-Test : (aka relationship test) evaluating if 2 samples taken from same grp are same or not
                            Mainly used for before vs after comparision
                        eg: students that took an extra math class scored had diff result second time, compared to first attempt
                            - for null hypothesis(h0) --> u(before) = u(after)           => there's no difference
                            - for alternative hypothesis(h1) --> u(before) != u(after)   => extra session is making an impact

c)Sample T-Test : evaluating if the average of a single grp is different from the known population average
                 Population mean is usually a assumption from various resources
                 eg: article states that avg IQ of Indian adults = 110
                    We collect a sample from 'all states + adults'  then we evaluate against the known population avg

                For Population(X) and Sample(u)
                - for null hypothesis(h0) --> u(sample) = X   (chi)   => there's no difference - so artcile's claim is True
                - for alternative hypothesis(h1) --> u(before) != X   => there is a difference - article's claim is False

'''
#we also need to import 'scipy' library for this 
import scipy.stats as sts

#Indepenedent sample t-test exercise:       A/B Test
'''Imagine you work for a e-commerce company and your team is responsible for optimizing company's website
    to increase user engagement and sales. Current design of 'Buy Now' button is being tested against a new 
    design to see if it performs better than old one '''


'''Randomly selected website users are divided into GroupA vs GroupB (independent of eachother)

    Give GroupA old button and GroupB new button then :
    - measure usage scores
    - perform independent t-test 
    
    
    Null Hypothesis : uA = uB  (there is no difference between old and new website) 
    Alternative Hypothesis : uA != uB (new website is causing an impact)
    
    '''

import numpy as np
import pandas as pd
import scipy.stats as sts

df = pd.read_csv("/home/vinayakgaur07/Downloads/Book.csv")

#calculate p-value:  probability of a statement from a sample being true
p_val = sts.ttest_ind(df['Group A'], df['Group B'])[1]
#               |                                   |
#       (t-test independent)               p-value comes as 2nd output, so use index 1 

#cuz p-value gives 3 outputs: t-statistics, p-value, degree of freedom

'''
T-Statistics --> How big the difference is between the two groups compared to how spread out the data is within each group.
p-value --> The chance that the difference you found happened purely by luck if there wasn't a real difference in the world.
Degree of freedom --> The number of data points you can change without breaking the rules of your calculation
'''

print('p-value =',p_val)    #p-value: 0.004496033893359867


#without index mentioned:
p_val = sts.ttest_ind(df['Group A'], df['Group B'])   
print('Outputs: ',p_val)      
#Outputs: TtestResult(statistic=-3.164120928510628, pvalue=0.004496033893359867, df=22.0)

#[0]:statistics
#[1]:p-value
#[2]:df



#Critical Value at 5%:
alpha = 0.05

#evaluation step:
if p_val > alpha:
    print("We do not reject NUll Hypothesis, so there is no change from new button")
else:
    print("We reject Null Hypothesis, so there is a change from new button")


#what if we want to perform a evaluation with a direction ? eg:the results are higher or lower 
#This is called One-sided Test or One-Tailed Test(the one we just did is called Two-sided Test)

'''
2 Sided-Test --> graph has tails on both sides 
1 Sided-Test --> a) Upper Tail(right side)
                 b) Lower Tail(left side)
'''

#we dont need to split alpha into half in one-sided test
'''
Therefore, null and alternative hypothesis:
-H0:  uB <= uA (new button is performing similar or worse than older)
-H1:  uB > uA (new button is performing better)
 '''

#if we choose greater , then the order matters so B needs to be mentioned first:
p_val = sts.ttest_ind(df['Group B'], df['Group A'], alternative='greater')[1]
print('p-value: ',p_val)

if p_val < alpha:
    print("We reject NUll hypothesis. Grp B has a positive impact on engagement")
else:
    print("We failed to reject NUll hypothesis. Grp B has no impact or less")


#---Paired Sample T-Test Exercise:
'''for a particular hospital it is adverrtised that a particular chemotherapy session
does not change patient's health based on blood pressure.It is to be checked if bp before 
treatment is equal to bp after treatment for same person. Perform a statistical significance
at alpha = 0.05 to help validate the claim 

H0: u(before) = u(after) --> there is no impact with chemo
H1: u(before) != u(after) --> there is an impact on bp

'''

def HypoTesting(p_val, alpha = 0.05): #default to alpha = 5%
    if(p_val > alpha):
        print("We do not reject Null Hypothesis")
    else:
        print("We reject Null Hypothesis")


df = pd.read_csv("/home/vinayakgaur07/blood_pressure.csv")
print(df.head())
#    patient   sex agegrp  bp_before  bp_after
# 0        1  Male  30-45        143       153
# 1        2  Male  30-45        163       170
# 2        3  Male  30-45        153       168
# 3        4  Male  30-45        153       142
# 4        5  Male  30-45        146       141

p_val = sts.ttest_rel(df['bp_before'], df['bp_after'])[1]       #relative test, not independent (cuz its the same person)
HypoTesting(p_val)          #We reject Null Hypothesis
#therefore, there is an impact on bp after chemotherapy 


#One-sample T-test exercise:
#Problem statement: 
'''
For a particular organization, the avg age of employee was clamied 30 years. The authorities collected random sample of 10 
employees age data to check claim made by organization.Construct hypothesis test to validate hypothesis at significance level 
of 5%

For X=30 (Population mean):
H0: uS = 30 (there is no difference and the claim is correct)
H1: uS != 30 (claim is incorrect)
'''

df = pd.read_csv("/home/vinayakgaur07/Documents/Ages.csv")


                                    #---- Z-Test ----#
'''
- Used for 2 variables or 1 variable against the population mean
- When the sample size is large (>30) OR the standard deviation of the population is known

eg: 
school principal claims that student are more intelligent than those of other schools
A random sample of 50 student's IQ scores has a mean score of 110. The mean population 
IQ is 100 with standard deviation of 15. State whether claim of principalis right or not
at a 5% significance level

H0: uS = XS (there is no difference in IQ, and  claim is false)
H1: uS != XS (claim is partially true )

List of givens:
sample info:
    mean = 110
    sample size = 50

population info:
    mean = 100
    pop standard deviation = 15

evaluation:
    alpha = 0.05 (5%)

Since we know standard deviation of population and size > 50, then we use z-test

Challenge here is -> we dont have data but do have its metrics
Therefore, trick is to generate a dataset based on metrics that we assume that resembles the original data
(assumming data has a normal distribution)

To generate a sample, we need to have standard deviation 
to derive it we use formula:
    (std deviation of sample) = (std deviation of population) / (square root of sample size)

'''
import math         #this comes with python

#Givens:
alpha = 0.05

sample_mean = 110
sample_size = 50            #we need sample_std

pop_mean = 100
pop_std = 15


#sample std formula:
sample_std = pop_std/math.sqrt(sample_size)         #math.sqrt(value) --> used for finding sqrt

print("Sample Standard Deviation = ",sample_std)

#-Now that we have standard deviaion of sample we can use Numpy's 'normal()' func

#used to draw random samples from a normal distribution:
student_sample = np.random.normal(loc=sample_mean, scale=sample_std, size=sample_size)

#loc: The mean or center of the distribution, where the peak of the bell curve is located. The default is 0
#scale: The standard deviation 'sigma' or "width" of the distribution, which determines the spread of the data around the mean. A larger scale results in a flatter, wider curve.The default is 1
#size: The shape of the output array. If None (default), it returns a single value. Otherwise, it returns a NumPy array with the specified dimensions. 

#output of np.random.normal:
# [108.01286841 110.68972872 107.59741123 110.55748594 109.47715394
#  108.70797445 113.16745942 110.04204874 109.3548139  108.02965309
#  108.91060569 107.3673988  111.48157972 105.17977658 110.4898589
#  106.71390155 106.21201202 107.69731877 110.85589918 108.45712514
#  108.06902933 109.08236466 105.70478027 111.6234856  110.08464282
#  107.37695206 111.05561516 116.94063449 109.72578981 110.07120788
#  105.49238042 111.74952201 111.19998262 112.14675994 112.19032491
#  113.26527018 108.66010222 113.81172214 106.87622978 107.92116317
#  111.39042469 109.75256579 108.12308053 111.18414476 111.81827382
#  106.11185685 106.60022983 108.50378261 109.68473167 112.60057187]


len(student_sample)         #50 --> no.of random samples
np.mean(student_sample)     #110.39067078826267 --> mean of all random samples 

'''eg:
Here is how you use it to generate '1000' samples with a mean of '50' and standard deviation '10':

=> sample = np.random.normal(loc= 50, scale= 10, size= 1000)
                                |           |           |
                               mean        std     no.of samples
'''

#For advanced z-testing we use another library of python --> 'statsmodels'
#install using 'pip install statsmodels'

from statsmodels.stats.weightstats import ztest

p_val = ztest(student_sample, value=pop_mean)[1]        #--> p-value also comes here at 2nd position
HypoTesting(p_val)

'''Result:  we reject null hypothesis, therefore the principal claim is True-we dont know '''

#to evaluate larger vs smaller:
'''
H0: uS <= XS (avg IQ of students is less than or equal to general population)
H1: uS > XS (claim is correct and claim is True )'''

p_val = ztest(student_sample, value=pop_mean, alternative='larger')[1] 


                            #---Chi-Square Distribution & Test---#
#symbol for it : (X^2) --> square of chi
'''
It is a continuous probability distribution
(Normal distribution is also a continuous probability distribution)

Characteristics:
- Non-negative values(always squared)
- Positively skewed graph --> shows a Rejected region(c) and a Accepting region(1-c)

It's used to test Independence: determine whether 2 categorical variables are associated or not 
Only for t-stat & z-stat, name of the statistical result of chi-square test is called chi-stat

Steps to perform chi-square test:
1) Define null & alternative hypothesis
     - H0: there is no relationship
     - H1: there is a relationship between the 2 variables (Group A & Group B are associated/dependent with eachother)

2) Build the contingency table
3) Calculate p-val using 'chi2_contingency()' func
4) Define alpha
5) Compare p-val to alpha
'''

# ---Exercise---#
'''Let's say we gathered survey for favorite car color between man & women. We want to find out if there's any association between 
   gender and favorite car color '''
# ---Solution---#
''' H0: there is no relationship between the 2 variables
    H1: there is a relationship between the 2 variables
'''
df = pd.read_csv("/home/vinayakgaur07/Downloads/Shopping.csv")

df['gender'].value_counts()          #Male 20 ; Female  20
df['car_color'].value_counts()        
# Black     10
# Silver     9
# White      8
# Red        7
# Grey       6


#step 1: done(defining H0 & H1)
#step 2: contingency table --> using cross-tab func

cont_table = pd.crosstab(df['gender'], df['car_color'])

# car_color  Black  Grey  Red  Silver  White
# gender                                    
# Female         3     2    7       6      2
# Male           7     4    0       3      6

'''Interpretation of contingency table:
    - 2 Females like Grey color car
    - 6 Males like White color car
'''
 
#step 3: using 'chi2_contingency()' func
'''
The chi2_contingency() func gives 4 results: 
1. chi statistic
2. p-value
3. dof(degree of freedom)
4. expected frequency
'''

chi_stat, p_val, dof, exp_freq = sts.chi2_contingency(cont_table)
#this line means that we are storing the 4 results into these 4 variables respectively in order

print(p_val)  #gives p-value
alpha = 0.05

HypoTesting(p_val, alpha) #we reject null hypothesis
#therefore, there is a relation between gender and color of car that they choose
#we can double check our findings when we inspect the expected 

print(exp_freq)
#this gives us what the statistical model expect the contingency table to look like if there's no relationship/association
#for comparision we format exp_freq to readable format using dataframe 

exp_freq_df = pd.DataFrame(data = exp_freq,
                           columns = df['car_color'].unique(),
                           index = df['gender'].unique())
#         Black  Silver  White  Red  Grey
# Male      5.0     3.0    3.5  4.5   4.0
# Female    5.0     3.0    3.5  4.5   4.0

#now this is what the statistical model expect when there is no relation 
#expected frequency above state that the values above satisfy the null hypothesis(no relation)

#compare this with original table and observe the difference in value 
 
                        #---ANOVA---#
'''
stands for = ANnalysis Of VAriance

It assesses whether mean of multiple groups are statistically significant from eachother or not 
z-test and t-test are limited to 2 variables/groups for evaluation, ANOVA can do 2 or more
Statistical result of ANOVA is called f-statistic (from its inventor, Fisher)

Types of ANOVA:
-One-way ANOVA --> deals with 1 factor/measure or groups eg: student with IQ(factor) between Class 1,2 and 3
-Two-way ANOVA --> deals with 2 factors/measures or groups eg: student with IQ and age (2 factors) between Class 1,2 and 3
-MANOVA (Multi-way ANOVA) --> deals with multiple factors for multiple groups

Although ANOVA can analyze 2 groups still it is recommended to use t & z tests for it cuz they are easier to interpret and they provide direction also

Steps for ANOVA:(One-way)
1. Define Hypothesis statement:
        -H0: there is no statistically significant difference between all groups 
        -H1: there is a statistically significant difference between all groups 

2. Set alpha value
3. Calculate p-value 
4. Run the evaluation 
'''

        #Exercise#
'''Suppose you are a researcher conducting an agricultural study to compare yield of 3 different fertilizer treatments(Treatment A, Treatment B, Treatment C)
    on a specific type of crop. You want to determine if there is a significant difference in crop yields among the treatments '''

        #Solution#
df = pd.read_csv("/home/vinayakgaur07/Downloads/crop_yield.csv")
#step 1:
#H0: there is no significant difference in crop yields among treatments 
#H1: there is a significant difference in crop yields among treatments 

#step 2:
alpha = 0.05   #5%

#step 3:
anova = sts.f_oneway(df['Treatment_A'], df['Treatment_B'], df['Treatment_C'])    # 1 way anova(represented by f) based p-value 
# F_onewayResult(statistic=162.20772086808603, pvalue=9.385801303950258e-49)

#we use index [1] to collect p-value from anova:
p_val = sts.f_oneway(df['Treatment_A'], df['Treatment_B'], df['Treatment_C'])[1]    #9.385801303950258e-49

# .f_oneway() --> this is the specific function within scipy.stats that performs a One-Way ANOVA F-test.
# determine if there are any statistically significant differences between the means of three groups

#step 4:
HypoTesting(p_val)          #we reject null hypothesis
#therefore, there is a significant difference in crop yields among the treatments.



            #--- Mann-Whitney U-Test ---#
'''
-z and t tests only work when we have normal or close to normal distribution(light skewness is okay)
-In a scenario where distribution cannot be fixed and is inconsistent (far from bell-curve shape), we consider using 'Non-parametric evaluation(Mann-Whitney U-Test)'

Non-parametric evaluation means: 
    - you cannot rely on standard statistical measures to interpret the data such as mean, median, std deviation, etc...
    - the distribution doesn't help as it doesn't follow the normal distribution
That's when we use Mann-Whitney U-Test

For null and alternative hypotheses:
    -H0: there is no difference between grp A & B
    -H1: there is a difference between grp A & B

Atleast 1 variable should be non-normal to consider Mann-Whitney U-Test

Examples:
Evaluate salaries of post-graduate students from 2 diff universities and check if they are different from eachother(based in 5% critical value)
'''
df = pd.read_csv("/home/vinayakgaur07/Salary_sample.csv")
df.hist()       #shows histrogram 
#we see inconsistency by plotting them and then observing 
# so we cannot use t or z test and therefore use Mann-Whitney U-Test

#Mann-Whitney U-Test for p-value(indexing):
p_val = sts.mannwhitneyu(df['University_X'], df['University_Y'])[1]

HypoTesting(p_val)          #result: we reject null hypothesis
#therefore there is a difference between salaries of post-graduates from 2 diff universities 

#Mann-Whiteny U-Test only works for 2 variables, for more than 2 variables we use KRUSKAL-WALLIS Test






