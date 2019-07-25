import pandas as pd
import math

data=pd.read_excel('E:\\python\\project\\user_reviews.xlsx')


applications=set()
for application in data["App"]:
    applications.add(application)
#print(applications)

app=(data["App"])
sentiment=(data["Sentiment"])
pd.options.mode.chained_assignment=None
for i in range(len(sentiment)):
    if sentiment[i] =="Positive":
        sentiment[i]=1
    if sentiment[i] =="Negative":
        sentiment[i]=-1
    if sentiment[i] =="Neutral":
        sentiment[i]=0
    if math.isnan(sentiment[i]):
        sentiment[i]=0.0
#print(sentiment)

summ=c=0
senti={}
for i in applications:
    for j in range(len(data["App"])):
        if i==app[j]:
            summ+=sentiment[j]
            c+=1
    #print(summ,c)
    senti.update({i:summ})
    c=0
    summ=0
#print(senti)
maximum=max(senti,key=senti.get)
print("Highest maximum average ratings is {} and corresponding category is {}".format(senti[maximum],maximum)) 


minimun=min(senti,key=senti.get)
print("Highest minimun average ratings is {} and corresponding category is {}".format(senti[minimun],minimun)) 
