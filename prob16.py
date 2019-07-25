import pandas as pd
import numpy as np
import re


def prob16():
    data=pd.read_excel('E:\\python\\project\\App-data.xlsx')
    yr=data["Last Updated"].tolist()
    month=[]
    year=[]
    strr=[]
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

    
    grp1=data.groupby(["Month","Year"])
    month_year=grp1["installs"].agg(np.sum).to_dict()
    print(grp1["installs"].agg(np.sum))
    
    grp2=data.groupby("Year")
    year=grp2["installs"].agg(np.mean)
    del year['1.0.19']
    print(year)
    months=[]
    for k,v in year.items():
        print(k,v)
        for i,j in month_year.items():
            if i[1]==k:
                if v-5<=j<=v+5:
                    months.append(i[0]+"of year"+i[1]+" is the best indicator to avg download that app will generate in"+i[1])
                
    return months           
    
    
#prob16()

