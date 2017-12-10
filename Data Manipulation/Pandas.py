from multiprocessing.sharedctypes import _new_value

import pandas as pd

#create a data frame - dictionary is used here where keys get converted to column names and values to row values.
from builtins import print

data = pd.DataFrame({'country':['Ind','SL','AUS','US'],'Rank':[1,2,3,4]})
print (data)

#We can do a quick analysis of any data set using:
print(data.describe())
#To get the complete information about the data set, we can use info() function.
print(data.info())

#Let's create another data frame.
data = pd.DataFrame({'group':['a', 'a', 'a', 'b','b', 'b', 'c', 'c','c'],'ounces':[4, 3, 12, 6, 7.5, 8, 3, 5, 6]})
print (data)

#Let's sort the data frame by ounces - inplace = True will make changes to the data

print (data.sort_values(by=['ounces'],ascending=True,inplace=False))

print (data.sort_values(by=['group','ounces'],ascending=[True,False],inplace=False))

#we get data sets with duplicate rows, which is nothing but noise.
#we get rid of such inconsistencies in the data set
#create another data with duplicated rows
data = pd.DataFrame({'k1':['one']*3+['two']*4, 'k2':[3,2,1,3,3,4,4]})
print (data)
data.sort_values(by='k1')
print (data)
print (data.drop_duplicates())
print (data.drop_duplicates(subset='k1'))

data = pd.DataFrame({'food': ['bacon', 'pulled pork', 'bacon', 'Pastrami','corned beef', 'Bacon', 'pastrami', 'honey ham','nova lox'],
                 'ounces': [4, 3, 12, 6, 7.5, 8, 3, 5, 6]})
print(data)
#we want to create a new variable which indicates the type of animal which acts as the source of the food

meat_to_animal ={
    'bacon':'pig',
'pulled pork': 'pig',
'pastrami': 'cow',
'corned beef': 'cow',
'honey ham': 'pig',
'nova lox': 'salmon'
}

def meat_2_animal(series):
    if series['food'] == 'bacon':
        return 'pig'
    elif series['food'] == 'pulled pork':
        return 'pig'
    elif series['food'] == 'pastrami':
        return 'cow'
    elif series['food'] == 'corned beef':
        return 'cow'
    elif series['food'] == 'honey ham':
        return 'pig'
    else:
        return 'salmon'

#create a new variable
data['animal']=data['food'].map(str.lower).map(meat_to_animal)
print(data)

#another way of doing it is: convert the food values to the lower case and apply the function
lower = lambda x:x.lower()
data['food']=data['food'].apply(lower)
data['animal2'] = data.apply(meat_2_animal, axis='columns')
print(data)

#Another way to create a new variable is by using the assign function

print(data.assign(new_variable=data['ounces']*10))
data.drop('animal2',axis='columns',inplace=True)
print(data)

#A quick method for imputing missing values is by filling the missing value with any random number.
##Series function from pandas are used to create arrays
data=pd.Series([1., -999., 2., -999., -1000., 3.])
print(data)
import numpy as np
#replace -999 with NaN values
data.replace([-999,-1000], np.nan,inplace=True)
print(data)

data = pd.DataFrame(np.arange(12).reshape((3, 4)),index=['Ohio', 'Colorado', 'New York'],columns=['one', 'two', 'three', 'four'])
print(data)
#Using rename function
data.rename(index = {'Ohio':'texas'},columns={'one':'one_p','two':'two_p'},inplace=True)
print(data)
data.rename(index = str.upper, columns=str.title,inplace=True)
print(data)

#Next, we'll learn to categorize (bin) continuous variables.
ages = [20, 22, 25, 27, 21, 23, 37, 31, 61, 45, 41, 32]
bins = [18, 25, 35, 60, 100]
cats = pd.cut(ages, bins)
print(cats)
#To include the right bin value, we can do:
print(pd.cut(ages,bins,right=False))
#pandas library intrinsically assigns an encoding to categorical variables.
print(cats.labels)

print(pd.value_counts(cats))

bin_names = ['Youth', 'YoungAdult', 'MiddleAge', 'Senior']
new_cats = pd.cut(ages, bins,labels=bin_names)
print(pd.value_counts(new_cats))

#Let's proceed and learn about grouping data and creating pivots in pandas. ' \
#It's an immensely important data analysis method which you'd probably have to use on every data set you work with.
df=pd.DataFrame({'key1':['a', 'a', 'b', 'b', 'a'],
                   'key2' : ['one', 'two', 'one', 'two', 'one'],
                   'data1' : np.random.randn(5),
                   'data2' : np.random.randn(5)})
print(df)
#calculate the mean of data1 column by key1
grouped = df['data1'].groupby(df['key1'])
print(grouped.mean())

dates = pd.date_range('20130101',periods=6)
df = pd.DataFrame(np.random.randn(6,4),index=dates,columns=list('ABCD'))
print(df)
#get first n rows from the data frame
print(df[:3])
#slice based on date range
print(df['20130101':'20130104'])
#slicing based on column names
df.loc[:,['A','B']]
#slicing based on both row index labels and column names
print(df.loc['20130102':'20130103',['A','B']])
#slicing based on index of columns
#returns 4th row (index is 3rd)
print(df.iloc[3] )

#we can copy the data set
df2 = df.copy()
df2['E']=['one', 'one','two','three','four','three']
print(df2)

#select rows based on column values
print(df2[df2['E'].isin(['two','four'])])

#list all columns where A is greater than C
print(df.query('A > C'))

#Pivot tables are extremely useful in analyzing data using a customized tabular format
#create a data frame
data = pd.DataFrame({'group': ['a', 'a', 'a', 'b','b', 'b', 'c', 'c','c'],
                 'ounces': [4, 3, 12, 6, 7.5, 8, 3, 5, 6]})
print(data)

#calculate means of each group
print(data.pivot_table(values='ounces',index='group',aggfunc=np.mean))

#calculate count by each group--based on AGGfunc
print(data.pivot_table(values='ounces',index='group',aggfunc='count'))







