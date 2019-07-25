import pandas as pd
import numpy as np

def three_yrs():
    data=pd.read_excel("E:\\python\\project\\App-data.xlsx")
    yr=data["Last Updated"].tolist()
    for i in range(len(yr)):
        year=yr[i].split(",")
        yr[i]=year[-1]
    
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
    ser2=pd.Series(yr)
    data["Year"]=ser2
    del data["Last Updated"]
    
    newyr=data.groupby("Year")
    newyr1=newyr.get_group(" 2016")
    ans1=newyr1["installs"].agg(np.sum)
    print(ans1)
    newyr2=newyr.get_group(" 2018")
    ans2=newyr2["installs"].agg(np.sum)
    print(ans2)
    string=[]
    sol=(ans2-ans1)*100/ans1
    print(sol)
    if sol<0:
        string.append("There is a percentage decrease of {} over the period of three years".format(abs(sol)))
    else:
        string.append("There is a percentage increase of {} over the period of three years ".format(sol))
#----------------------------------YEAR 2016------------------------------------------------           
    newyr=data.groupby("Year")
    newyr2=newyr.get_group(" 2016")
    sol=newyr2.groupby("Category")
    ans=sol["installs"].agg(np.sum).to_dict()
    #print(ans)
    maximum=max(ans,key=ans.get)
    minimum=min(ans,key=ans.get)
    string.append("HIGHEST DOWNLOADS IN 2016 IS {} AND CORRESPONDING CATEGORY IS is {}".format(ans[maximum],maximum)) 
    string.append("LOWEST DOWNLOADS IN 2016 IS {} AND CORRESPONDING CATEGORY IS is {}".format(ans[minimum],minimum)) 

#----------------------------------YEAR 2017------------------------------------------------        
    newyr=data.groupby("Year")
    newyr2=newyr.get_group(" 2017")
    sol=newyr2.groupby("Category")
    ans=sol["installs"].agg(np.sum).to_dict()
    #print(ans)
    maximum=max(ans,key=ans.get)
    minimum=min(ans,key=ans.get)
    string.append("HIGHEST DOWNLOADS IN 2017 IS {} AND CORRESPONDING CATEGORY IS is {}".format(ans[maximum],maximum)) 
    string.append("LOWEST DOWNLOADS IN 2017 IS {} AND CORRESPONDING CATEGORY IS is {}".format(ans[minimum],minimum)) 

#----------------------------------YEAR 2018------------------------------------------------        
    newyr=data.groupby("Year")
    newyr2=newyr.get_group(" 2018")
    sol=newyr2.groupby("Category")
    ans=sol["installs"].agg(np.sum).to_dict()
    #print(ans)
    maximum=max(ans,key=ans.get)
    minimum=min(ans,key=ans.get)
    string.append("HIGHEST DOWNLOADS IN 2018 IS {} AND CORRESPONDING CATEGORY IS is {}".format(ans[maximum],maximum)) 
    string.append("LOWEST DOWNLOADS IN 2018 IS {} AND CORRESPONDING CATEGORY IS is {}".format(ans[minimum],minimum)) 
    
    return string

