import pandas as pd
from collections import OrderedDict
import numpy as np


def prob10():
    strr=[]

    data=pd.read_excel("E:\\python\\project\\App-data.xlsx")
    yr=data["Last Updated"].tolist()
    categories=set()
    for category in data["Category"]:
        categories.add(category)
    month=[]
    year=[]
    for i in range(len(yr)):
         y=yr[i].split(',')
         d=y[0][0:-2]
         month.append(d)
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

    grp1=data.groupby(["Category","Year","Month"])
    ans=grp1["installs"].agg(np.sum).to_dict()
    OrderedDict(ans)
#-----------------------------------month with max dwnd of each cat--------------------------------    
    
    md={}
    for cat in categories:
        for k in ans:
            if cat==k[0]:
                md.update({k:ans[k]})
        maximum=max(md,key=md.get)
        strr.append("{} has maximum downloads in month {} of year {} with download of {}".format(maximum[0],maximum[2],maximum[1],round(md[maximum])))
        md.clear()
     #   print(row)
    #val_list=[]

#------------------------------ratio of download, teen vs mature 17+--------------------------------------------    
    
    d=data.groupby("Content Rating")
    a=d.get_group("Teen")
    a1=a["installs"].agg(np.sum)
    #print(a1)
    
    d=data.groupby("Content Rating")
    b=d.get_group("Mature 17+")
    a2=b["installs"].agg(np.sum)
    #print(a2)
    strr.append("RATIO OF TEEN VS MATURE 17+ IS: {}".format(a1/a2))

    return strr


