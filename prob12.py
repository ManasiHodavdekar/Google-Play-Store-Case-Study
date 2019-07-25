import pandas as pd

def sentiments():
    data=pd.read_excel('E:\\python\\project\\user_reviews.xlsx')
    sentiment=data["Sentiment"].tolist()
    Apps=data["App"].tolist()
    apps=set()
    strr1=[]
    strr2=[]
    c=1
    strr2.append("Apps with same number of positive & negative sentiments are")
    print("Apps with same number of positive & negative sentiments are")
    for app in Apps:
        apps.add(app)
    track1={}
    track2={}
    for i in apps:
        start_index= Apps.index(i)
        length=Apps.count(i)
        track1.update({i:sentiment[start_index:start_index+length].count('Positive')})
        track2.update({i:sentiment[start_index:start_index+length].count('Negative')})
        if track1[i]==track2[i]:
            print(i)
        if c<=10:
            if track1[i]==track2[i]:
                strr2.append(i)
                c+=1
            #print(i)
        max1=max(track1,key=track1.get)
        max2=max(track2,key=track2.get)
    strr1.append("Most Positive sentiment is {} and corresponding App is {}".format(track1[max1],max1))
    strr1.append("Most Negative sentiment is {} and corresponding App is {}".format(track2[max2],max2))
    strr2.append("Etc. ")
    return strr1,strr2
#sentiments()
