import pandas as pd
import matplotlib.pyplot as plt
import math

def matplotCanvas(self):
    data=pd.read_excel('E:\\python\\project\\App-data.xlsx')
    
    app=data["App"].tolist()
    #print (app)
    installs=(data["Installs"])
    ratings=(data["Rating"])
    count=0
    for i in range(len(data["App"])):
        if installs[i]=="100,000+":
            if ratings[i]>=4.1:
                count=count+1
    print("Number of apps having 100,000+ downloads with 4.1+ rating is",count)
    pd.options.mode.chained_assignment=None
    for i in range(0,10841):
            if installs[i]=="1,000+":
                installs[i]=0.01
                continue
            if installs[i]=="5,000+":
                installs[i]=0.05
                continue
            if installs[i]=="10,000+":
                installs[i]=0.1
                continue
            if installs[i]=="50,000+":
                installs[i]=0.5
                continue
            if installs[i]=="100,000+":
                installs[i]=1.0
                continue
            if installs[i]=="500,000+":
                installs[i]=5
                continue
            if installs[i]=="1,000,000+":
                installs[i]=10
                continue
            if installs[i]=="5,000,000+":
                installs[i]=50
                continue
            if installs[i]=="50,000,000+":
                installs[i]=500
                continue
            if installs[i]=="10,000,000+":
                installs[i]=100
                continue
            else:
                installs[i]=0.0
    for i in range(len(ratings)):
        if math.isnan(ratings[i]):
            ratings[i]=0.0
            
    
    x=ratings.tolist()
    y=installs.tolist()
"""
print(y)
plt.figure(figsize=(15,9))
plt.scatter(x,y,'red')
plt.xlabel("Ratings")
plt.ylabel("Installs")
plt.xlim([0,5])#plt.xticks(np.arrange(0,3,0.250))
"""
f=Figure(figsize=(12,9),dpi=100)
a=f.add_subplot(111)
plt.scatter(x,y, c='blue')
#print(data)
plt.xlabel("Ratings")
plt.ylabel("Installs")
plt.xlim([0,7])
plt.ylim([0,2])
plt.show()
