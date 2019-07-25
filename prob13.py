import pandas as pd

def prob13(ans):
    data=pd.read_excel("E:\\python\\project\\user_reviews.xlsx")
    grp1=data.groupby(["App"])
    indices=grp1.groups[ans].tolist()
    apps=set()
    for app in data["App"]:
        apps.add(app)
    if ans in apps:
        f=1
    else:
        return 1,2
    
    #print(indices)
    x=[]
    y=[]
    for i in indices:
       x.append(data['Sentiment_Polarity'][i])
       y.append(data['Sentiment_Subjectivity'][i])
    return x,y
           

