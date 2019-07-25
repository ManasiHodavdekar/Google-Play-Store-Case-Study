import pandas as pd
df=pd.DataFrame()

def max_among():
    data=pd.read_excel("E:\\python\\project\\App-data.xlsx")
    categories=set()
    for category in data["Category"]:
        if category=="SPORTS":
            categories.add(category)
        if category=="ENTERTAINMENT":
            categories.add(category)
        if category=="SOCIAL":
            categories.add(category)
        if category=="NEWS":
            categories.add(category)
        if category=="EVENTS":
            categories.add(category)
        if category=="TRAVEL":
            categories.add(category)
        if category=="GAME":
            categories.add(category)
    print("The Categories are as follows", categories)
    
    installs = data["Installs"]
    pd.options.mode.chained_assignment=None
    for i in range(0,10841):
        for j in categories:
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
    c=0
    dwn=set()
    for inst in installs:
        dwn.add(category)
        
        
    for i in categories:
        for j in data["Category"]:
            if j==i:
                c+=1
                print("Downloads of {} is {}".format(categories,(installs*100000)))
max_among()