import pandas as pd

def prob17():
    data=pd.read_excel('E:\\python\\project\\App-data.xlsx')
    s=data["Size"].tolist()
    installs=data["Installs"].tolist()
    for i in range(len(s)):
        if s[i]=='Varies with device' or s[i]=='1,000+':
            s[i]='0'
        a=s[i].split('M')
        if s[i][-1]=='k':
            a=s[i].split('k')
            a[0]= round(0.001*float(a[0]))
        s[i]= float(a[0])
        
    for i in range(0,len(installs)):
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
    #print(installs)   
    
    y=[]
    temp1=temp2=temp3=temp4=temp5=temp6=temp7=temp8=temp9=temp10=temp11=temp12=temp=0
    temp13=temp14=temp15=temp16=temp17=temp18=0
    for i in range(len(s)):
        if 0<=s[i]<=5:
            temp1+=installs[i]
        if 5<=s[i]<=10:
            temp2+=installs[i]
        if 10<=s[i]<=15:
            temp3+=installs[i]
        if 15<=s[i]<=20:
            temp4+=installs[i]
        if 20<=s[i]<=25:
            temp5+=installs[i]
        if 25<=s[i]<=30:
            temp6+=installs[i]
        if 35<=s[i]<=40:
            temp7+=installs[i]
        if 40<=s[i]<=45:
            temp8+=installs[i]
        if 45<=s[i]<=50:
            temp9+=installs[i]
        if 50<=s[i]<=55:
            temp10+=installs[i]
        if 55<=s[i]<=60:
            temp11+=installs[i]
        if 60<=s[i]<=65:
            temp12+=installs[i]
        if 65<=s[i]<=70:
            temp13+=installs[i]
        if 70<=s[i]<=75:
            temp14+=installs[i]
        if 75<=s[i]<=80:
            temp15+=installs[i]
        if 80<=s[i]<=85:
            temp16+=installs[i]
        if 85<=s[i]<=90:
            temp17+=installs[i]
        if 90<=s[i]<=95:
            temp18+=installs[i]
        if s[i]>=95:
            temp+=installs[i]
    y.append(temp1)
    y.append(temp2)
    y.append(temp3)
    y.append(temp4)
    y.append(temp5)
    y.append(temp6)
    y.append(temp7)
    y.append(temp8)
    y.append(temp9)
    y.append(temp10)
    y.append(temp11)
    y.append(temp12)
    y.append(temp13)
    y.append(temp14)
    y.append(temp15)
    y.append(temp16)
    y.append(temp17)
    y.append(temp18)

    y.append(temp)
    #print(y)
    x=['0-5','5-10','15-20','20-25','25-30','30-35','35-40','40-45','45-50','50-55','55-60','60-65','65-70','70-75','75-80','80-85','85-90','90-95','95 and above']
    """
    plt.figure(figsize=(7,4))
    plt.scatter(x,y)
    plt.plot(x,y)
    plt.xlabel("Size in M")
    plt.ylabel("Installs")
    plt.xticks(rotation=90)
    plt.show()"""
    return x,y
#size_down()

