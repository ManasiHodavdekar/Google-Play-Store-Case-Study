import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import collections

data=pd.read_excel('E:\\python\\project\\App-data.xlsx')

"""final_Data={}
for i in data['Category']:
    x=i
    t1=(data[data.Category==i].Installs)
    print("------------------")
    print("Name of the Category=",i)
    print("Number of Installs",t1)
    final_Data.update({i : t1})
"""

df= pd.DataFrame(data,columns=['Category','Install'])
print(df.Category.unique()) 
seq=(df.Category.value_counts().tolist())
print(seq)
#sequence=list(zip(*[seq]))
percentages=[]
for x in seq:
    t=list(x)
    temp=[t.count(str(i))/len(x) for i in range(1,5)]  #work out the percentage of each number
    percentages.append(temp) #add percentages to list"""
