import pandas as pd

def range_down():
    data=pd.read_excel('E:\\python\\project\\App-data.xlsx')
    
    cat1=0
    cat2=0
    cat3=0
    cat4=0
    cat5=0
    installs=(data["Installs"])
    for i in range(len(data["App"])):
        if installs[i]=="10,000+" or installs[i]=="50000+":
            cat1=cat1+1
        if installs[i]=="50,000+" or installs[i]=="150,000+":
            cat2=cat2+1
        if installs[i]=="150,000+" or installs[i]=="500,000+":
            cat3=cat3+1
        if installs[i]=="500,000+" or installs[i]=="5,000,000+":
            cat4=cat4+1
        if installs[i]=="5,000,000+" or installs[i]=="50,000,000+":
            cat5=cat5+1
    sttrr=[]
    sttrr.append("a) Between 10,000 and 50,000 is {}".format(cat1))
    sttrr.append("b) Between 50,000 and 150000 is {}".format(cat2))
    sttrr.append("c) Between 150000 and 500000 is {}".format(cat3))
    sttrr.append("d) Between 500000 and 5000000 is {}".format(cat4))
    sttrr.append("e) More than 5000000 is {}".format(cat5))
    return sttrr 



