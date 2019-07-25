import pandas as pd

def no14(a):
    data=pd.read_excel('E:\\python\\project\\user_reviews.xlsx')

    sentiment=data["Sentiment"].tolist()
    Apps=data["App"].tolist()
    apps=set()
    print(sentiment)
    for app in Apps:
        apps.add(app)
