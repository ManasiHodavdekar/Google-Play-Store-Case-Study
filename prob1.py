import pandas as pd

def percent_down():
    data=pd.read_excel('E:\\python\\project\\App-data.xlsx')
    categories=set()
    for category in data["Category"]:
        categories.add(category)
    #print("The Categories are as follows", categories)
    #print("Number of categories =",len(categories))
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
            installs[i]=1
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
    #print(installs)
    #print(sum(installs))
    summ=0
    strr=[]
    for i in categories:
        for j in range(len(data["Category"])):
            if i== cat[j]:
                summ+=installs[j]
        strr.append("Percentage downloads of {} is {}".format(i,(summ*100)/sum(installs)))
        #strr.append("Percentage downloads of "+i+" is"+((summ*100)/sum(installs)))
        summ=0
    return strr