import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


points=np.arange(0,10,0.1)
# print(points)
sin=np.sin(points)
print(sin)
plt.plot(points,sin)
plt.xlabel('Points')
plt.ylabel('Sin Function')
plt.show()
# plt.close()
# plt.clf()
# plt.savefig('Sin Function')
# random_correlated_bivariate_state
# Generate a random correlated bivariate dataset
rs = np.random.RandomState(5)
mean = [0, 0]
cov = [(.5, 1), (1, .5)]
var1, var2 = rs.multivariate_normal(mean, cov, 500).T
var1 = pd.Series(var1, name="X-axis")
var2 = pd.Series(var2, name="Y-axis")

# Show the joint distribution using kernel density estimation
sns1 = sns.jointplot(var1, var2, kind="scatter")
plt.show()


#histogram
set1=np.random.randn(50)
plt.hist(set1,edgecolor='black',color='red',bins=20)
plt.show()
set2=np.random.rand(100)
plt.hist(set1,density=True,alpha=0.6,color='red',bins=20)
plt.hist(set2,density=True,alpha=0.6,bins=20)
plt.show()

set1=np.random.rand(50)
set2=np.random.randn(50)
sns2=sns.jointplot(set1,set2)#scatter
plt.show()
sns3=sns.jointplot(set1,set2,kind='hex')
plt.show()

set4=np.random.randint(0,100,size=(100,1))
print(set4)
sns.boxplot(set4,whis=np.inf)
plt.show()

set5=np.random.randn(50)
sns.boxplot(set5,whis=np.inf)
plt.show()


#Regression and subset of regression
df=pd.read_csv("C:\\Users\\gopib\\Downloads\\housing.csv")
print(df)
# print(df.columns.values)
# print(df.index.values)
sns.lmplot(x='total_bedrooms',y='median_house_value',data=df)
plt.show()
sns.lmplot(x='total_bedrooms',y='median_house_value',hue='ocean_proximity',data=df)
plt.show()


df1=pd.read_csv("C:\\Users\\gopib\\Downloads\\titanic training.csv")
df2=pd.read_csv("C:\\Users\\gopib\\Downloads\\titanic test.csv")
print(df1)
print(df2)
df3=pd.concat((df1,df2),axis=0)
print(df3)
df4=df1.append(df2,ignore_index=True)
print(df4)
df5=pd.read_csv("C:\\Users\\gopib\\Downloads\\housing.csv")
df5=df5[df5.ocean_proximity!='ISLAND']
df6=pd.pivot_table(df5,values='median_house_value',index=['housing_median_age'],columns='ocean_proximity')
sns.heatmap(df6)
# sns.heatmap(df6,annot=True)
plt.show()