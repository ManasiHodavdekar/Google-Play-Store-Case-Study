import pandas as pd

def prob14(a):
    stringp=[]
    stringne=[]
    stringn=[]
    stringp.append("========== POSITIVE REVIEWS ========== ")
    
    stringn.append("========== NEUTARL REVIEWS ==========")
    stringne.append("========== NEGATIVE REVIEWS ==========")
    data=pd.read_excel('E:\\python\\project\\user_reviews.xlsx')
    grp1=data.groupby(["App","Sentiment"]) 
    #a='Housing-Real Estate & Property'
    categories=set()
    for category in data["App"]:
        categories.add(category)
    if a in categories:
        f=1
    else:
        return 1,2,3
        
    p=grp1.groups[a, 'Positive'].tolist()
    for i in range(len(p)):
        stringp.append(str(data["Translated_Review"][p[i]]))
    ne=grp1.groups[a, 'Negative'].tolist()
    for i in range(len(ne)):
        stringne.append(str(data["Translated_Review"][ne[i]]))
    n=grp1.groups[a, 'Neutral'].tolist()
    for i in range(len(n)):
        stringn.append(str(data["Translated_Review"][n[i]]))
    
    return stringp,stringne,stringn 
