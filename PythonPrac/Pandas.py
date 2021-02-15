import pandas as pd
import numpy as np
s1=pd.Series([1,2,3,4])
print(s1)
print(s1)
print(s1.name)
print(s1.index.name)
#sets name of the series and index
s1.name='Test Values'
s1.index.name='Test Index'
print(s1.name)
print(s1.index.name)
print('----------')
s2=pd.Series([1,2,3,4],index=["India","USA","China","UK"])
print(s2)
print(s2.values)
print(s2.index.values)
index_list=["IN","US","CHN","GB"]
s2.index=index_list
print(s2)
t1=pd.Series([10,20,30,40,50],index=["UK","MEX","USA","IN","CHN"])
t1.name='Population Density'
t1.index.name="Country Code"
t2=pd.Series([2,4,6],index=["IN","US","MEX"])
t3=t1/t2
print(t3)
print(t3.isnull())
print('---------------')
print(t3.notnull())
print('------------')
print(t3[t3>=20])
print(t3[t3!=20])
df=pd.read_csv('C:\\Users\\gopib\\Downloads\\international-migration-nz.csv')
print(df.head())
print(df.tail(3))
print(df['status'])
print('-------------')
print(str(type(df['status'])))
new_df=pd.DataFrame(df['standard_error'])
print(new_df)
print(df.columns)
print(df.loc[0])
new_df=pd.DataFrame(df,columns=['year_month','new_column'])
print(new_df)
new_df['new_column']=0
print(new_df)
new1_df=pd.DataFrame(df.head(),columns=['year_month','new_column'])
# filling NaN
new1_df['new_column']=10
#adding a new column
new1_df['new_column2']=0
print(new1_df)
#adding new column with Series
new1_df['new_column3']=pd.Series(np.random.random(5))
print(new1_df)
#adding new column with arange
new1_df['new_column4']=np.arange(0,5,1)
print(new1_df)
new1_df['Random_ID'] = np.arange(new1_df.shape[0])
print(new1_df)
print(new1_df.iloc[0])
print(new1_df.loc[1])
df_sample=pd.DataFrame({'Player':['Puji','Virat','Jaddu','Ash'],
                        'Average':[55,54,34,44],
                        'Wickets':[0,2,90,200]
                        },index=['P','V','J','A'])
print(df_sample)
print(df_sample.loc['P'])
print(df_sample.loc['P':'J']) #J included
print(df_sample.iloc[0])
print(df_sample.iloc[0:2])#2 not included
print("------------")
print(df_sample.iloc[0:2]['Average'])
print(df_sample.iloc[0:2,0:2])
print(df_sample.loc[(df_sample.Average>50) &(df_sample.Wickets==0)])
# print(df_sample.iloc[(df_sample.Wickets>0)]) -will result in error as iloc does not accept boolean indexing
df_sample.loc[(df_sample.Average>50),['Wickets']]=0
print(df_sample)
df_sample.loc[(df_sample.Average)>50,['Wickets']]=2
print(df_sample)
print(df_sample.loc['P':'J',['Average']])
print(df_sample.iloc[0:2,0:2])
print('--------')
print(df_sample.iloc[0:2,0:2]['Average'])
s1=pd.Series([10,20,30,40,50],index=['A','B','D','E','F'])
s1.name='Sample'
s1.index.Name='Index'
print(s1)
s2=s1.reindex(index=['A','B','C','D','E','F','G'])
print(s2)
s3=s2.ffill()
print(s3)
s4=pd.Series([1,2,3,4,5],index=['a','b','c','d','e'])
s5=s4.reindex(['a','b','c','d','e','f'],fill_value=0)
print(s5)
df_1=pd.DataFrame(np.arange(16).reshape(4,4),index=['R1','R2','R4','R5'],columns=['C1','C2','C4','C5'])
print(df_1)
df_2=pd.DataFrame({'Player':['P1','P2','P4','P5'],
                   'Year':[2002,2003,2005,2006],
                   'Points':[600,200,400,500]},index=['IND','AUS','RSA','NZ'])
print(df_2)
print(df_2.loc['IND':'RSA',['Player','Points']])
print(df_2.iloc[0:2,0:2])
print(df_2.loc[(df_2.Points>100) &(df_2.Year<=2005)])
df_2.loc[df_2.Player=='P2',['Points']]=250
print(df_2)
df_2=df_2.reindex(index=['IND','AUS','IRE','RSA','NZ'])
print(df_2)
df_2=df_2.reindex(columns=['Player','Year','Points','Total Points'])
print(df_2)
df_2=df_2.ffill(axis=0)
print(df_2)
df_2=df_2.ffill(axis=1)
print(df_2)
df_2=df_2.rename({'IRE':'ENG'})
print(df_2)
df_2=df_2.rename(columns={'Total Points':'MVP_Points'})
print(df_2)
df_2.loc['ENG']=['P3',2004,200,200]
print(df_2)
df_2.loc[df_2.Player=='P4',['Points']]=225
# df_2.loc['RSA']=['P4x']
# print(df_2)
df_2.loc['RSA',['MVP_Points']]=225
print(df_2)
#select and drop entries in a series
ser1=pd.Series([11,2,3,4,5],index=['A','B','C','D','E'])
print(ser1['A'])
print(ser1[0]) #element at index 0
print(ser1[ser1>2])
print(ser1.loc["B":"C"])
print(ser1.iloc[0:2])
print(ser1[1:])
ser1=ser1.drop(['D','E'])
ser1=ser1.drop('C')
print(ser1)
# df_3=pd.DataFrame(data={'Player':['Ricky','Sachin','Lara','Border','Gavaskar','Donald'],
#                         'Runs':[11000,16000,12000,11000,10000,9000]},index=['AUS','IND','WI','AUS','IND','AUS'])
#No error with above
df_3=pd.DataFrame(data={'Player':['Ricky','Sachin','Lara','Border','Gavaskar','Donald'],
                        'Runs':[11000,16000,12000,11000,10000,9000]},index=['AUS','IND','WI','AUS_EX','IND_EX','AUS_EX2'])
print(df_3)
print('----------')
print(df_3.loc['AUS'])
print(df_3.loc['AUS']['Runs'])
print(df_3.iloc[0:2,0:2])
print(df_3.loc[df_3.Runs>10000])
print(df_3.loc[df_3.Player=='Ricky'])
df_3=df_3.reindex(['AUS','IND','WI','AUS_EX','IND_EX','AUS_EX2','WI_EX'])
df_3.loc['WI_EX']=['Viv',9000]
print(df_3)
df_3=df_3.reindex(columns=['Player','Runs','Avg'])
df_3=df_3.reindex(['Player','Runs','Avg','SR'],axis=1)
print(df_3)
df_3=df_3.drop(['AUS_EX2','WI_EX'])
print(df_3)
df_3=df_3.drop(['Avg','SR'],axis=1)
print(df_3)
#Sorting and Ranking
se1=pd.Series(np.random.random(5),index=[1,2,3,4,5])
se1.index.name='IDX'
print(se1)
new_index=6
index_val=se1.index.values
print(index_val)
index_val=index_val.tolist()
print(index_val)
index_val.append(new_index)
print(index_val)
se1=se1.reindex(index=index_val)
print(se1)
print(se1.sort_index())
print(se1.sort_values())
print(se1.rank())
#Append and Concat
df_new=pd.DataFrame(np.arange(25).reshape(5,5))
print(df_new)
df_new2=pd.DataFrame(np.arange(25,30).reshape(1,5))
df_new=df_new.append(df_new2,ignore_index=True)
print(df_new)
df_new1=pd.concat([pd.DataFrame([i], columns=['A']) for i in range(5)],
          ignore_index=True)
print(df_new1)
df_new3=pd.DataFrame(np.arange(5,10).reshape(5,1))
df_new1['B']=0
print(df_new1)
df_new1.loc[5]=[5,0]
print(df_new1)

#Dealing with missing data
s1=pd.Series([1,2,np.NaN])
print(s1)
print(s1.isnull())
print(s1.notnull())


df=pd.DataFrame(data={'Player':[1,2,3,4,5]})
print(df)
df=pd.DataFrame(np.arange(4),columns=['A'])
print(df)
df=pd.DataFrame(np.arange(4).reshape(1,4),columns=list('ABCD'))
print(df)
null_val=np.nan
df=pd.DataFrame([[1,2,3,4,5],[null_val,7,8,9,null_val],[null_val,null_val,null_val,null_val,null_val],[10,null_val,null_val,null_val,11]])
print(df)
print(df.isnull())
print(df.notnull())
print(df)
print(df.dropna()) #same as with axis=0 , drops rows with atleast one Nan
print(df.dropna(axis=1)) #drops columns with atleast one Nan, so dropping everything here in this eg
print(df.dropna(how='all')) #deletes where all values are nan
print(df.dropna(thresh=1)) #returns rows which have atleast one non Nan Value
print(df.fillna(0))
print(df)
df=df.rename({0: 'A',1:'B',2:'C',3:'D'})
print(df)
df.loc['B']=df.loc['B'].fillna(0)
print('------')
print(df)
print(df[4])
df[4]=df[4].fillna(0)
print(df)
df=df.fillna(0)
print(df)
print(df.sum(axis=0))
print(df.sum(axis=1))
print(df.min(axis=0))
print(df.min(axis=1))
print('---------')
print(df.idxmin(axis=0))
print(df.idxmin(axis=1))
print(df.idxmax(axis=0))
print(df.idxmax(axis=1))
s1=pd.Series(np.random.random(5),index=[['A','A','B','B','B'],[1,2,1,2,3]])
print(s1)
df=pd.DataFrame(np.arange(25).reshape(5,5),index=[['IND','IND','AUS','AUS','AUS'],['DAY1','DAY1','DAY2','DAY2','DAY2']]
                ,columns=[['DEC','DEC','MAR','MAR','MAR'],['WIN','WIN','LOSS','LOSS','LOSS']])
print(df)
df=pd.DataFrame(np.arange(25).reshape(5,5),columns=list('ABCDE'))
print(df)

# print(df.shape[0],df.shape[1])
print(len(df.index))#faster than shape
print(len(df.columns))
minrow=df.min(axis=1)
maxrow=df.max(axis=1)
mincol=df.min(axis=0)
maxcol=df.max(axis=0)
print(minrow)
print(maxrow)
print(minrow+maxrow)
print(mincol+maxcol)
df['row_sum']=minrow+maxrow
print(df)
df.loc['column_sum']=mincol+maxcol
print(df)


def Sum_Swap(df):
    # Write code here!
    minrow = df.min(axis=1)
    maxrow = df.max(axis=1)
    mincol = df.min(axis=0)
    maxcol = df.max(axis=0)
    df['row_sum'] = mincol + maxcol
    df.loc['col_sum'] =  minrow + maxrow
    print(df)
    return df
df=pd.DataFrame([[12,2,3,44],[40,1,34,9],[6,99,56,69],[2,24,4,71]])
Sum_Swap(df)
#Educative Code
# def Sum_Swap(df):
#     minm_r = np.min(df, axis=1)  # Get minimum elements from all rows
#
#     maxm_r = np.max(df, axis=1)  # Get maximum elements from all rows
#
#     df['row_sum'] = minm_r + maxm_r  # Add the min & max values and assign them to new column
#
#     minm_c = np.min(df, axis=0)  # Get minimum elements from all columns
#
#     maxm_c = np.max(df, axis=0)  # Get maximum elements from all columns
#
#     df.loc['col_sum'] = minm_c + maxm_c  # Add the min & max values and assign them to new row
#
#     a, b = df['row_sum'].copy(), df.loc['col_sum'].copy()  # Store values of row and column in temparory variables
#
#     df['row_sum'], df.loc['col_sum'] = b, a  # Interchange the values
#
#     return df
#
#
# # Test Code
#
# df = pd.DataFrame(np.random.randint(1, 100, 25).reshape(5, 5))
#
# df_res = Sum_Swap(df.copy())
#
# print(df_res)
import pandas as pd

srs1 = pd.Series([1, 2, 3], index = ['A', 'B', 'C'])
srs2 = pd.Series([4, 5, 6], index = ['C', 'D', 'B'])
print(srs1 + srs2)


# x = range(0,11)
# print(x)


Rv = np.linspace(0.0, 20.0, 100)
print(Rv)

x = np.random.randint(0, 1000, size = (1, 1000))[0]
print(x)

resamples = [np.random.choice(x, size = 25, replace = True) for i in range(30)]
print(resamples)
print('\n-----------------------------------------------')
df=pd.read_csv("C:\\Users\\gopib\\Downloads\\MSFT.csv")
print(df.head())
print(df['Date'])
print(df.loc[0])

df=pd.DataFrame([[1,2,3,4,5],[null_val,7,8,9,null_val],[null_val,null_val,null_val,null_val,null_val],[10,null_val,null_val,null_val,11]])
print(df)
print(df.isnull())
print(df.notnull())
print(df)
print(df.dropna()) #same as with axis=0 , drops rows with atleast one Nan
print(df.dropna(axis=1)) #drops columns with atleast one Nan, so dropping everything here in this eg
print(df.dropna(how='all')) #deletes where all values are nan
print(df.dropna(thresh=1)) #returns rows which have atleast one non Nan Value
print(df.fillna(0))
print(df)
df=df.rename({0: 'A',1:'B',2:'C',3:'D'})
print(df)
df[0]=df[0].fillna(0)
print(df)
df=pd.DataFrame(np.arange(1,26).reshape(5,5))
print(df)
df=df.rename({0:'A',1:'B',2:'C',3:'D',4:'E',5:'F'})
print(df)
df=df.reindex(['A','B','C','D','E','F'])
print(df)
df[5]=np.NaN
print(df)
df=df.ffill(axis=0)
print(df)
df=df.ffill(axis=1)
print(df)
df.loc['F',[4]]=20
print(df)
df=df.rename(columns={0:'a'})
print(df)
df=df.rename({'A':'Aa'})
print(df)
df.loc['G']={'a':25,1:25,2:2,3:5,4:5}
print(df)