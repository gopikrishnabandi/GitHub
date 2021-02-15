import numpy as np
import pandas as pd


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
print('Actual Df')
print(df)
stacked_df=df.stack()
print('Stacked Df')
print(stacked_df)
print('Unstacked Df')
print(stacked_df.unstack())
print('-------------')
print(stacked_df.unstack('Row'))
print('-------------')
print(stacked_df.unstack('Column'))