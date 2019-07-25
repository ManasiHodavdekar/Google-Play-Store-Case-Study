import pandas as pd
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
#from matplotlib.backends.backend_tkagg import NavigationToolbas2TkAgg
import math
from tkinter import*
class Root(Tk):    
    def __init(self):
        super(Root,self).__init__()
        self.title("Graph")
        self.minsize(640,400)
        self.wm_iconbimap('icon.ico')
        self.matplotCanvas()
    def data_req(self):
        data=pd.read_excel('E:\\python\\project\\App-data.xlsx')
        global x,y
        #app=data["App"].tolist()
        #print (app)
        installs=(data["Installs"])
        ratings=(data["Rating"])
        count=0
        for i in range(len(data["App"])):
            if installs[i]=="100,000+":
                if ratings[i]>=4.1:
                    count=count+1
        print("Number of apps having 100,000+ downloads with 4.1+ rating is",count)
        pd.options.mode.chained_assignment=None
        for i in range(0,10841):
                if installs[i]=="1,000+":
                    installs[i]=0.01
                    continue
                if installs[i]=="5,000+":
                    installs[i]=0.05
                    continue
                if installs[i]=="10,000+":
                    installs[i]=0.1
                    continue
                if installs[i]=="50,000+":
                    installs[i]=0.5
                    continue
                if installs[i]=="100,000+":
                    installs[i]=1.0
                    continue
                if installs[i]=="500,000+":
                    installs[i]=5
                    continue
                if installs[i]=="1,000,000+":
                    installs[i]=10
                    continue
                if installs[i]=="5,000,000+":
                    installs[i]=50
                    continue
                if installs[i]=="50,000,000+":
                    installs[i]=500
                    continue
                if installs[i]=="10,000,000+":
                    installs[i]=100
                    continue
                else:
                    installs[i]=0.0
        for i in range(len(ratings)):
            if math.isnan(ratings[i]):
                ratings[i]=0.0
                
        
        x=ratings.tolist()
        y=installs.tolist()
    
    def matplotCanvas(self):
        self.data_req()
        f=Figure(figsize=(12,9))
        a=f.add_subplot(111)
        a.plot(x,y)
        canvas=FigureCanvasTkAgg(f,self)
        canvas.show()
        canvas.get_tk_widget().pack(side=BOTTOM, fill=BOTH,expand=TRUE)
        
if __name__=='__main__':
    root=Root()
    root.mainloop()
"""
print(y)
plt.figure(figsize=(15,9))
plt.scatter(x,y,'red')
plt.xlabel("Ratings")
plt.ylabel("Installs")
plt.xlim([0,5])#plt.xticks(np.arrange(0,3,0.250))
"""