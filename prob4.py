import pandas as pd
import numpy as np

def max_avgrating():
    data=pd.read_excel("E:\\python\\project\\App-data.xlsx")
    r=data.groupby('Category')
    #print(r.groups)
    rat= r["Rating"].agg(np.mean).to_dict()
    #print(rat)
    string1=[]
    string2=[]
    for cat,rating in rat.items():
        string1.append("Average of {} is {}".format(cat,rating))
    maximum=max(rat,key=rat.get)
    string2.append("HIGHEST MAXIMUM AVERAGE RATING IS {} AND CORRESPONDING CATEGORY IS is {}".format(rat[maximum],maximum)) 
    return string1,string2  
#max_avgrating()
