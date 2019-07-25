import pandas as pd

def prob5(ans):
    data=pd.read_excel("E:\\python\\project\\App-data.xlsx")
    date=data["Last Updated"].tolist()
    installs = data["Installs"].tolist()
    categories=set()
    for category in data["Category"]:
        categories.add(category)
    if ans in categories:
        f=1
    else:
        return 1,2
    
    for i in range(len(installs)):
        if installs[i]=="1,000+":
            installs[i]=0.1
            continue
        if installs[i]=="5,000+":
            installs[i]=0.5
            continue
        if installs[i]=="10,000+":
            installs[i]=1
            continue
        if installs[i]=="50,000+":
            installs[i]=5
            continue
        if installs[i]=="100,000+":
            installs[i]=10
            continue
        if installs[i]=="500,000+":
            installs[i]=50
            continue
        if installs[i]=="1,000,000+":
            installs[i]=100
            continue
        if installs[i]=="5,000,000+":
            installs[i]=500
            continue
        if installs[i]=="50,000,000+":
            installs[i]=5000
            continue
        if installs[i]=="10,000,000+":
            installs[i]=1000
            continue
        else:
            installs[i]=0.0
    ser1=pd.Series(installs)
    data["installs"]=ser1  
    del data["Installs"]  
    
    grp1=data.groupby(["Category"])
    indices=grp1.groups[ans].tolist()
    y=list()
    x=list()
    for i in indices:
        y.append(data['installs'][i])
        x.append(pd.to_datetime(data["Last Updated"][i]))
    x.sort()
    return x,y
    
