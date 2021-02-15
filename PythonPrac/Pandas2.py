import numpy as np
import pandas as pd
import seaborn as sbn
import matplotlib.pyplot as plt
from scipy.stats import *

df=pd.read_csv("C:\\Users\\gopib\\Downloads\\MSFT.csv")
print(df)
print(df.isnull().any())
# df.loc[0,'Date']=np.NaN
# print(df.isnull().any())
# Nan_rows_list=[]
# for index,row in df.iterrows():
#   is_Nan_Series=row.isnull()
#   if is_Nan_Series.any():
#       Nan_rows_list.append(index)
# print(Nan_rows_list)
df.to_csv("C:\\Users\\gopib\\Downloads\\MSFT_dup.csv")
df=pd.Series([1,2,3,4,5,6],index=[['a','b','b','c','c','c'],['r1','r2','r2','r3','r3','r3']])
print(df)
df=pd.DataFrame({
    'Puji':[1,2,3,4,5,6]
    ,'Ashwin':[7,8,9,10,11,12]},index=[[1,2,2,3,3,3],[4,5,5,6,6,6]])
print(df)
df1=pd.DataFrame({'Player':['Puji','Rahul','Sachin','Puji','Sanga']
                 ,'Runs_one':[50,65,70,100,45]})
df2=pd.DataFrame({'Player':['Puji','Rahul','Sachin','Sourav','Ricky']
                 ,'Runs_two':[50,65,70,100,45]})
df3=pd.DataFrame({'Runs_three':[55,62,72,102,44]},index=['Puji','Rahul','Sachin','Sourav','Sourav'])
print(pd.merge(df1,df2))
print(pd.merge(df1,df2,how='left'))
print(pd.merge(df1,df2,how='right'))
print(pd.merge(df1,df2,how='outer'))
print(pd.merge(df1,df3,left_on='Player',right_index=True))
print(pd.merge(df3,df1,left_index=True,right_on='Player'))
print('---------------------')
df_tests=pd.DataFrame({'Tourney Top Scorer':['Pujara','Kohli','Kane','Root','Smith','Kohli'],
                       'Top Score tests':[151,152,153,154,155,156]})
df_odis=pd.DataFrame({'Tourney Top Scorer':['Warner','Kohli','Smith','Rohit','Kohli'],
                      'Top Score odi':[141,142,143,144,145]})
df_classA=pd.DataFrame({'List A top Score':[171,172,173,174,175]},index=['Kane','Kohli','Jason Roy','Stokes','Rohit'])

print(pd.merge(df_tests,df_odis))
print(pd.merge(df_tests,df_odis,how='left'))
print(pd.merge(df_tests,df_odis,how='right'))
print(pd.merge(df_tests,df_classA,left_on='Tourney Top Scorer',right_index=True))
df=pd.DataFrame([1,2,3,4,5,6],index=[['a','b','b','c','c','c'],['d','e','e','f','f','f']],columns=['A'])
print(df)
print(df.stack())
df=pd.DataFrame(np.arange(25).reshape(5,5),index=['a','b','c','d','e'],columns=['c1','c2','c3','c4','c5'])
df.index.name='Row'
df.columns.name='Column'
print(df)
stacked_df=df.stack()
print(stacked_df)
print(stacked_df.unstack())
print(stacked_df.unstack('Row'))
print(stacked_df.unstack('Column'))

##Pivoting
df=pd.DataFrame({'Puji':[1,2,3,4,5],'Kohli':[7,8,9,10,11],'Jinx':[12,13,14,15,16]})
df.index.name='Series'
df.columns.name='Player'
print(df)
print(df.pivot('Puji','Kohli','Jinx'))

df = pd.DataFrame({'Company': ['Google', 'Microsoft', 'Google', 'Microsoft'],
      'Product': ['Editor', 'Editor', 'Calendar', 'Azure'],
      'Price': ['$200', '$250', '$50', '$400']})

df.index.name = 'Row'
df.columns.name = 'Column'

print("The Original DataFrame")
print(df,'\n')

print("The Pivoted DataFrame")
print(df.pivot('Company', 'Product', 'Price'))

map_hq={'Google':'Mountain View','Microsoft':'Seattle'}
df['Headquaters']=df['Company'].map(map_hq)
print(df)

df=pd.DataFrame({'Client':['BSC','TFS','Cisco','Microsoft'],
                 'Domain':['Health','Automobile Insurance','Manufacturing','Technology']
                                  })
df.index.name='Infy Clients'
df.columns.name='Details'
print(df)
df=df.rename({0:'a',1:'b',2:'c',3:'d'})
print(df)
loc_map={'BSC':'Oakland','TFS':'LA','Cisco':'San Jose'}
df['Location']=df['Client'].map(loc_map)
print(df)
df.loc['d',['Location']]='Seatle'
print(df)
df.loc[df.Client=='Microsoft',['Location']]='Redmond'
print(df)
df.loc['e']=['BP','Energy','London']
print(df)
df.loc['f']=['BP','Energy','London']
print(df)
print(df.drop_duplicates())
df.loc['BP',['Location']]='Redmond'
print(df)
print(df.drop_duplicates(['Location']))
print(df)
df=df.reindex(['a','b','c','d','e','f','g'])
print(df)
df.loc['f',['Client']]='Apple'
print(df)
print(df.drop_duplicates(['Location']))


S1=pd.Series([1,2,2,3,3,3,1,2],index=['a','b','c','d','e','f','g','h'])
S1=S1.replace(1,np.NaN)
print(S1)
S1=S1.rename({'a':'A'})
print(S1)
S1=S1.rename(index=str.upper)
print(S1)

df=pd.DataFrame({'a':[1,2,3,4,5],'b':[6,6,8,9,10]})
print(df)
df=df.replace(6,7)
print(df)
df=df.replace((6,9),(7,10))
print(df)
df=df.rename(index={0:'A'},columns={'a':'c'})
print(df)
df = pd.DataFrame(np.random.randn(900,3))
print(df)
quantiles_df=(df.quantile([0.25,0.75]))
print(quantiles_df)
# print(quantiles_df.loc[0.25][0])
Q1=quantiles_df[0][0.25]
print(Q1)
Q3=quantiles_df[0][0.75]
print(Q3)
IQR=Q3-Q1
lower_bound=(Q1-(IQR*1.5))
upper_bound=(Q3+(IQR*1.5))
print(lower_bound)
print(upper_bound)
column_one=df[0]
print('outliers')
print(column_one[(column_one<lower_bound)])
print(column_one[(column_one>upper_bound)])
column_one[(column_one<lower_bound)]=lower_bound
column_one[(column_one>upper_bound)]=upper_bound
# print(column_one[column_one==lower_bound])


df=pd.DataFrame(np.random.rand(10000,5))
quantiles_df=df.quantile([0.25,0.75])
print(quantiles_df)
Q1=quantiles_df[0][0.25]
Q3=quantiles_df[0][0.75]
IQR=Q3-Q1
upper_bound=Q3+1.5*IQR
lower_bound=Q1-1.5*IQR
column_one=df[0]
column_one[column_one<lower_bound]=lower_bound
column_one[column_one>upper_bound]=upper_bound
print(column_one)

S1=pd.Series([1,2,3,4,5,6], index=['a', 'b', 'b', 'c', 'c','c'],name='max speed')
print(S1.groupby(level=0).mean())
S1=pd.Series([1,2,3,4,5,6], name='max speed')
print(S1.groupby(['a', 'b', 'b', 'c', 'c','c']).mean())

df=pd.DataFrame({'Player':['p1','p2','p1','p2','p3','p3','p4'],
                 'Team':['t1','t2','t1','t2','t3','t4','t5'],
                 'Runs':[10,20,30,40,50,60,70]
                 },index=['a','b','c','d','e','f','g'])
print(df)
print(df.groupby('Player'))
print(df.groupby('Player').sum())
print(df.groupby('Team'))
print(df.groupby('Team').sum())
print(df.groupby(['Player','Team']).mean())
print(df.groupby(['Player','Team']).sum())

import random

df=pd.DataFrame({'Animal':[random.choice(['Hen','Pig','Ox','Fish','Shrimp']) for i in range(15)],
                 'Protein':[random.choice(range(10,20)) for i in range(15)],
                 'weight':[random.choice(range(20,100)) for i in range(15)],
                 'Fat Percent':abs(np.random.randn(15))})

print(df)
# print(np.random.randn(15).shape)
var=df.groupby('Animal')
print(var)
print(var.agg('sum'))
print(var.agg('mean'))
print(var.agg('describe'))
print(var.agg('last'))
print(var.agg('std'))
print(var.agg('var'))
print(var.agg('count'))

def rank_func(df):
    df['Rank']=np.arange(0,len(df),1)+1
    return df


df=pd.read_csv('C:\\Users\\gopib\\Downloads\\AirQualityUCI.csv')
print(df)
df=df.drop_duplicates()
print(df.describe())
df=df.dropna(thresh=1)
print(df)
df=df.drop(columns=['Unnamed: 15','Unnamed: 16'])
print(df)
df=df.sort_values(['NO2(GT)','CO(GT)'],ascending=False)
print(df)
df=df.groupby('Date')
print(df)
df=df.apply(rank_func)
df=df[df.Rank==1]
print(df)
print(df.sort_index())

"""-------------------------"""

df=pd.read_csv('C:\\Users\\gopib\\Downloads\\housing.csv')
print(df)
df=df.dropna(axis='rows')
print(df)
df_quantile=df.quantile([0.25,0.75])
print(df_quantile)

Q1_median_house_value=df_quantile['median_house_value'][0.25]
# print(Q1_median_house_value)
Q3_median_house_value=df_quantile['median_house_value'][0.75]
IQR1=Q3_median_house_value-Q1_median_house_value
upper_bound_mhv=Q3_median_house_value+(1.5*IQR1)
lower_bound_mhv=Q1_median_house_value-(1.5*IQR1)
df[df.median_house_value<lower_bound_mhv]=lower_bound_mhv
df[df.median_house_value>upper_bound_mhv]=upper_bound_mhv

Q1_median_income=df_quantile['median_income'][0.25]
Q3_median_income=df_quantile['median_income'][0.75]
IQR2=Q3_median_income-Q1_median_income
upper_bound_mi=Q3_median_income+(1.5*IQR2)
lower_bound_mi=Q1_median_income-(1.5*IQR2)
df[df.median_income<lower_bound_mi]=lower_bound_mi
df[df.median_income>upper_bound_mi]=upper_bound_mi

Q1_hma=df_quantile['housing_median_age'][0.25]
Q3_hma=df_quantile['housing_median_age'][0.75]
IQR3=Q3_hma-Q1_hma
upper_hma=Q3_hma+(1.5*IQR3)
lower_hma=Q1_hma-(1.5*IQR3)
df[df['housing_median_age']<lower_hma]=lower_hma
df[df.housing_median_age>upper_hma]=upper_hma

print(df)
#
# df1=pd.read_csv('C:\\Users\\gopib\\Downloads\\housing.csv')
#
# def clean_data(df):
#
#     df = df.dropna()
#
#     out_list = ['median_house_value', 'median_income', 'housing_median_age']
#
#     quantiles_df = (df.quantile([0.25,0.75]))
#
#     for out in out_list:
#
#         Q1 = quantiles_df[out][0.25]
#         Q3 = quantiles_df[out][0.75]
#
#         iqr = Q3 - Q1
#
#         lower_bound = (Q1 - (iqr * 1.5))
#         upper_bound = (Q3 + (iqr * 1.5))
#
#         col = df[out]
#
#         col[(col < lower_bound)] = lower_bound
#
#         col[(col > upper_bound)] = upper_bound
#
#     return df
# print(clean_data(df1))