import pandas as pd
from collections import Counter
import numpy as np
import re


def prob11():
    data=pd.read_excel("E:\\python\\project\\App-data.xlsx")
    yr=data["Last Updated"].tolist()
    month=[]
    year=[]
    for i in range(len(yr)):
        st=""
        y=yr[i].split(',')
        ans= re.findall("\D",y[0])
        for j in range(len(ans)):
            st=st+ans[j]
        month.append(st)
        year.append(y[-1])
    ser1=pd.Series(month)
    data["Month"]=ser1   
    ser2=pd.Series(year)
    data["Year"]=ser2
    del data["Last Updated"]     
    
    years=set()
    for y_r in data["Year"]:
        years.add(y_r)
    installs = data["Installs"].tolist() 
    #pd.options.mode.chained_assignment=None
    for i in range(len(installs)):
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
            installs[i]=5.0
            continue
        if installs[i]=="1,000,000+":
            installs[i]=10.0
            continue
        if installs[i]=="5,000,000+":
            installs[i]=50.0
            continue
        if installs[i]=="50,000,000+":
            installs[i]=500.0
            continue
        if installs[i]=="10,000,000+":
            installs[i]=100.0
            continue
        else:
            installs[i]=0.0
            
    ser1=pd.Series(installs)
    data["installs"]=ser1   
    del data["Installs"]  

    grp1=data.groupby(["Year","Month"])
    ans=grp1["installs"].agg(np.sum).to_dict()
    #print(ans)
    md={}
    strr=[]
    for i in years:
        for k in ans:
            if i==k[0]:
                md.update({k:ans[k]})
        k=Counter(md)
        high=k.most_common(3)
        
        #print("Month {} ,{} and {} of year {} has Maximum number of downloads".format(high[0][0][1],high[1][0][1],high[2][0][1],high[0][0][0]))
        for j in high:
            #print("{} of {} year has Maximum number of downloads ".format(j[0][1],j[0][0]))
            strr.append("{} of {} year has Max number of downloads ".format(j[0][1],j[0][0]))
        #print("\n")
        md.clear()
    print (strr)
    return strr
#prob11()
