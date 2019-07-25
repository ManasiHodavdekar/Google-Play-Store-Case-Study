import pandas as pd
import numpy as np

def prob7():
     string=[]
     data=pd.read_excel('E:\\python\\project\\App-data.xlsx')
     installs = data["Installs"].tolist() 
     
     yr=data["Last Updated"].tolist()
     year=[]
     for i in range(len(yr)):
        y=yr[i].split(',')
        year.append(y[-1])   
     ser2=pd.Series(year)
     data["Year"]=ser2
     del data["Last Updated"]     
    
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
            
     av=data.groupby("Android Ver")
     varyd=av.get_group("Varies with device")    
     grp1=varyd.groupby("Year")
     a=grp1["installs"].agg(np.sum).to_dict()
     #print(a)
     start=a[' 2012']
     final=a[' 2018']
     sol=((final-start)*100)/start
     if sol<0:
         string.append("There is a percentage decrease of {}".format(abs(sol)))
     else:
         string.append("There is a percentage increase of {}".format(abs(sol)))
         
     return string
     
#prob7()

