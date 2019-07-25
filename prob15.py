import pandas as pd

def prob15(a):
    data=pd.read_excel('E:\\python\\project\\user_reviews.xlsx')

    sentiment=data["Sentiment"].tolist()
    Apps=data["App"].tolist()
    apps=set()
    #print(sentiment)
    for app in Apps:
        apps.add(app)   
    dictt={}
    for i in apps:
        start_index= Apps.index(i)
        length=Apps.count(i)
        p=sentiment[start_index:start_index+length].count('Positive')
        n=sentiment[start_index:start_index+length].count('Negative')
        if p>n:
            dictt.update({i:"is Advisable"})
        else:
            dictt.update({i:"is Not Advisable"})
            
    #print(dictt)
    flag=0
    strr=[]
    #a=input("Enter the name of the app :")
    if a in dictt.keys():
        flag=1
    if flag==1:
        strr.append("The app "+dictt[a])
        
    return strr