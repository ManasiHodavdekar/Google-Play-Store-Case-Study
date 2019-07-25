import pandas as pd

def Additional2(apname,apver):
    print(apname,apver)
    strr=[]
    data=pd.read_excel("E:\\python\\project\\App-data.xlsx")
    df=data["Android Ver"]
    av=list()
    for i in range(len(df)):
        y=str(df[i]).split('and up')
        av.append(y[0][0:-1])
    
    ser1=pd.Series(av)
    data["AV"]=ser1   
    del data["Android Ver"]
    #print(data)
    grp1=data.groupby("App") 
    g=grp1.get_group(apname)
    av_ofapp=g["AV"].tolist()
    i=0
    flag=False
    while i<=len(apver):
       if i==0 and int(apver[i])>int(av_ofapp[0][i]) :
           flag=True
           break
       if int(apver[i])>=int(av_ofapp[0][i]):
           if i==len(apver)-1:
                flag=True
           i+=2   
       else:
           strr.append("App {} cannot run on your device".format(apname))
           return strr
    if flag:
       strr.append("App {} can run on your device".format(apname))
       return strr
#Additional2("Kids Paint Free - Drawing Fun","4.0.2")