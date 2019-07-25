import pandas as pd
import numpy as np
import re
import matplotlib.pyplot as plt

def probAdditional(a):
    #a.insert(0," ")
    data=pd.read_excel("E:\\python\\project\\App-data.xlsx")
    yr=data["Last Updated"].tolist()
    year=[]
    for i in range(len(yr)):
        st=""
        y=yr[i].split(',')
        ans= re.findall("\D",y[0])
        for j in range(len(ans)):
            st=st+ans[j]
        year.append(y[-1])
    ser2=pd.Series(year)
    data["Year"]=ser2
    del data["Last Updated"]     
    installs = data["Installs"].tolist() 
    #pd.options.mode.chained_assignment=None
    for i in range(len(installs)):
        if installs[i]=="1,000+":
            installs[i]=1
            continue
        if installs[i]=="5,000+":
            installs[i]=5
            continue
        if installs[i]=="10,000+":
            installs[i]=10
            continue
        if installs[i]=="50,000+":
            installs[i]=50
            continue
        if installs[i]=="100,000+":
            installs[i]=100
            continue
        if installs[i]=="500,000+":
            installs[i]=500
            continue
        if installs[i]=="1,000,000+":
            installs[i]=1000
            continue
        if installs[i]=="5,000,000+":
            installs[i]=5000
            continue
        if installs[i]=="50,000,000+":
            installs[i]=50000
            continue
        if installs[i]=="10,000,000+":
            installs[i]=10000
            continue
        else:
            installs[i]=0.0
            
    ser1=pd.Series(installs)
    data["installs"]=ser1   
    del data["Installs"]  

    df=data.groupby(["Year","Category"])
    ans=df["installs"].agg(np.sum).to_dict()
    #print(ans)
    x=[]
    y=[]
    for i in ans:
        if i[0]==a:
            x.append(i[1])
            y.append(ans[i])#d.update({i: df.groups[i]})
    return x,y
