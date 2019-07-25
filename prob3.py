import pandas as pd
def average():
    data=pd.read_excel("E:\\python\\project\\App-data.xlsx")
    categories=set()
    for category in data["Category"]:
        categories.add(category)
    #print("The Categories are as follows", categories)
    print("Number of categories =",len(categories))
    installs = data["Installs"]
    cat=data["Category"]
    
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
    gre={}
    avg={}
    c=summ=0
    for i in categories:
        for j in range(len(data["Category"])):
            if i==cat[j]:
                summ+=installs[j]
                c+=1
        gre.update({i:summ})
        avg.update({i:(summ/c)})
        summ=0
        c=0
    strr=[]
    maxx=max(gre,key=gre.get)
    minn=min(gre,key=gre.get)
    strr.append("Category with most downloads is {}".format(maxx))
    strr.append("Category with least downloads is {}".format(minn))
    strr.append("Category with average of at least 2,50,000 downloads are: ")
    for j in avg.keys():  
        if (avg[j]*100000)>=250000:
            strr.append(j)
    return strr