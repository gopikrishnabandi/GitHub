import numpy as np
import pandas as pd
# np.random.seed(144848)
x=np.random.randint(0,1000,size=(1,1000))[0]
# print(random)
sample=[np.random.choice(x,size=25,replace=True) for i in range(30)]
# print(sample)
list=[]
for i in range(30):
    list.append(sample[i].mean())
print(list)
list_mean=sum(list)/len(list)
print(list_mean)
x_mean=x.mean()
print(x_mean)