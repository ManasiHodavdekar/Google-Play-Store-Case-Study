from prob1 import*
from prob2 import*
from prob3 import*
from prob4 import*
from prob6 import*
from prob5 import*
from prob7 import*
from prob9 import*
from prob10 import*
from prob11 import*
from prob12 import*
from prob13 import*
from prob14 import*
from prob15 import*
from prob16 import*
from prob17 import*
from prob18 import*
from probAdditional import*
from Additional2 import*
from tkinter import*
import pandas as pd
from tkinter import Tk,messagebox,StringVar,IntVar,Label,Radiobutton,Entry,Checkbutton,Button,OptionMenu,Toplevel,Message
from tkinter import simpledialog
from tkinter.ttk import Combobox
from matplotlib import pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk

def adjustWindow(window):
     w = 800 
     h = 500 
     ws = root.winfo_screenwidth() 
     hs = root.winfo_screenheight() 
     x = (ws/2) - (w/2) 
     y = (hs/2) - (h/2)
     window.geometry('%dx%d+%d+%d' % (w, h, x, y)) 
     window.resizable(False, False)
     window.configure(background='#2E1114')
                      
def sol1():
    s=percent_down()
    messagebox.showinfo("Analysis",',\n'.join(s),parent=window2)
def sol2():
    s=range_down()
    messagebox.showinfo("Analysis",',\n'.join(s),parent=window2)
def sol3():
    s=average()
    messagebox.showinfo("Analysis",',\n'.join(s),parent=window2)
def sol4():
    s1,s2=max_avgrating()
    messagebox.showinfo("Analysis",',\n'.join(s1),parent=window2)
    messagebox.showinfo("Analysis",',\n'.join(s2),parent=window2)
def sol5():
    ans=simpledialog.askstring("Input","Enter the name of category",parent=window2)
    x,y=prob5(ans)
    if x==1:
        messagebox.showerror("Analysis","App "+ans+" did not Found ",parent=window2)
    else:       
        graph1=Tk()
        graph1.title("Observed Trend")
        graph1.geometry("1000x500")
        f=Figure(figsize=(10,5),dpi=100)
        a=f.add_subplot(111)
        a.plot(x,y,color="red",linewidth=1,alpha=0.9)
        canvas=FigureCanvasTkAgg(f,graph1)
        canvas.draw()
        canvas.get_tk_widget().place(x=0,y=0)
        toolbar=NavigationToolbar2Tk(canvas,graph1)
        toolbar.update()
        canvas.get_tk_widget().place(x=0,y=0)
        graph1.mainloop()
def sol6():
    s=three_yrs()
    messagebox.showinfo("Analysis",',\n\n'.join(s),parent=window2)
def sol7():
    s=prob7()
    messagebox.showinfo("Analysis",',\n'.join(s),parent=window2)
def sol9():
    graph1=Tk()
    graph1.title("Observed Trend")
    graph1.geometry("500x500")
    s,x=rate()
    messagebox.showinfo("Analysis",',\n'.join(s),parent=window2)
    f=Figure(figsize=(5,5),dpi=100)
    a=f.add_subplot(111)
    a.hist(x,bins=10842,edgecolor='black')
    canvas=FigureCanvasTkAgg(f,graph1)
    canvas.draw()
    canvas.get_tk_widget().place(x=0,y=0)
    toolbar=NavigationToolbar2Tk(canvas,graph1)
    toolbar.update()
    canvas.get_tk_widget().place(x=0,y=0)
    graph1.mainloop()
def sol10():
    s=prob10()
    messagebox.showinfo("Analysis",',\n'.join(s),parent=window2)
def sol11():
    s=prob11()
    messagebox.showinfo("Analysis" ,',\n'.join(s),parent=window2)
def sol12():
    s1,s2=sentiments()
    messagebox.showinfo("Analysis",',\n'.join(s1),parent=window2)
    messagebox.showinfo("Analysis",',\n'.join(s2),parent=window2)
def sol13():
    ans=simpledialog.askstring("Input","Enter the name of app",parent=window2)
    x,y=prob13(ans)
    if x==1:
        messagebox.showerror("Analysis","App "+ans+" did not Found ",parent=window2)
    else:       
        graph1=Tk()
        graph1.title("Observed Trend")
        graph1.geometry("1000x500")
        f=Figure(figsize=(10,5),dpi=100)
        a=f.add_subplot(111)
        a.scatter(x,y,color="red",alpha=0.9)
        canvas=FigureCanvasTkAgg(f,graph1)
        canvas.draw()
        canvas.get_tk_widget().place(x=0,y=0)
        toolbar=NavigationToolbar2Tk(canvas,graph1)
        toolbar.update()
        canvas.get_tk_widget().place(x=0,y=0)
        graph1.mainloop()

def sol14():
    ans=simpledialog.askstring("Input","Enter the name of app",parent=window2)
    s1,s2,s3=prob14(ans) 
    if s1==1:
        messagebox.showerror("Analysis","App "+ans+" did not Found ",parent=window2)
    else:         
        messagebox.showinfo("POSITIVE REVIEWS",' \n'.join(s1),parent=window2)
        messagebox.showinfo("NEGATIVE REVIEWS",' \n'.join(s2),parent=window2)
        messagebox.showinfo("NEUTRAL REVIEWS",' \n'.join(s3),parent=window2)
    graph1=Tk()
    graph1.title("Observed Trend")
    graph1.geometry("500x500")
    f= Figure(figsize=(5,5),dpi=100)
    a=f.add_subplot(111)
    #----------------------------------------------------------
    df=pd.read_excel("E:\\python\\project\\user_reviews.xlsx")
    d=df.groupby(["App","Sentiment"])
    p=d.groups[ans,"Positive"].tolist()
    ne=d.groups[ans,"Negative"].tolist()
    n=d.groups[ans,"Neutral"].tolist()
    x=["Positive","Negative","Neutral"]
    y=[len(p),len(ne),len(n)]
    #-------------------------------------------------
    a.bar(x,y)
    canvas= FigureCanvasTkAgg(f,graph1)
    canvas.draw()
    canvas.get_tk_widget().place(x=0,y=0)
    toolbar=NavigationToolbar2Tk(canvas,graph1)
    toolbar.update()
    canvas.get_tk_widget().place(x=0,y=0)
    graph1.mainloop()



def sol15():
    a=simpledialog.askstring("Input", "Enter the app name",parent=window2)
    s=prob15(a)
    messagebox.showinfo("Analysis",',\n'.join(s),parent=window2)
def sol16():
    s=prob16()
    messagebox.showinfo("Analysis",',\n\n'.join(s),parent=window2)
    
def sol17():
    graph1=Tk()
    graph1.title("Observed Trend")
    graph1.geometry("1300x500")
    x,y=prob17()
    f=Figure(figsize=(13,5),dpi=100)
    a=f.add_subplot(111)
    a.scatter(x,y)
    a.plot(x,y)
    canvas=FigureCanvasTkAgg(f,graph1)
    canvas.draw()
    canvas.get_tk_widget().place(x=0,y=0)
    toolbar=NavigationToolbar2Tk(canvas,graph1)
    toolbar.update()
    canvas.get_tk_widget().place(x=0,y=0)
    graph1.mainloop()
    
def add1():
    ans=simpledialog.askstring("Input","Enter the year",parent=window2)
    graph1=Tk()
    graph1.title("Observed Trend")
    graph1.geometry("700x700")
    x,y=probAdditional(ans)
    f=plt.figure(figsize=(11,11))
    explode=list()
    for k in x:
        explode.append(0.1)
    palette=["#FFC312","#C4E538","#12CBC4","#FDA7DF","#ED4C67","#F79F1F","#A3CB38","#1289A7","#D980FA","#B53471","#EE5A24","#009432","#0652DD","#9980FA","#833471","#EA2027","#006266","#1B1464","#5758BB","#6F1E51","#34495e","#95a5a6","#bdc3c7","#ecf0f1","#7bed9f","#FDA7DF","#D980FA","#fad390","#f8c291","#b8e994","#b71540","#be2edd","#fab1a0","#e58e26"]
    pie,text=plt.pie(y,labels=x,explode=explode,colors=palette,shadow=True)
    plt.legend(pie,x,loc="upper corner")
    canvas=FigureCanvasTkAgg(f,graph1)
    canvas.draw()
    canvas.get_tk_widget().place(x=0,y=0)
    toolbar=NavigationToolbar2Tk(canvas,graph1)
    toolbar.update()
    canvas.get_tk_widget().place(x=0,y=0)
    graph1.mainloop()
    
    
def mainscreen():
    global root
    root=Tk()
    adjustWindow(root)
    root.title("Google PlayStore App Launch Study")
    photo = PhotoImage(file="E:\python\project\\m88.png")
    label = Label(root,image=photo,text="")
    label.pack()
    label.image=photo
    Button(root, text="Proceed", bg="#e79700", width=20, height=2, font=("Open Sans",13, 'bold'), fg='white',command=downloads).place(x=100, y=350)
    root.mainloop()

def and_ver():
      ans1=simpledialog.askstring("Input","Enter the name of App and android version separated by comma",parent=window2)
      if ans1=="":
          messagebox.showerror("Error","Please fill all the details",parent=window2)
          ans1=simpledialog.askstring("Input","Enter the name of App and android version separated by comma",parent=window2)
      ans1,ans2=ans1.split(",")
      #print(type(ans1),type(ans2))
      ans=Additional2(ans1,ans2)
      print(ans)
      messagebox.showinfo("Analysis",ans[0],parent=window2) 
    
def downloads():
    global window2
    window2 = Toplevel(root)
    window2.title("Questions")
    adjustWindow(window2)
    first()

def first():
    Label(window2, text="", bg='#2E1114',width='800', height='500').place(x=0, y=0)
    Label(window2,text="1) What is the percentage download in each category on the playstore",font=("Times", 15),fg='white',bg="#2E1114").place(x=1,y=20)
    b1=Button(window2,text="Solution 1",font=("Times", 10),bd=5,command=sol1)
    b1.place(x=700, y=20)
    Label(window2,text="2) How many apps have managed to get the following number of downloads",font=("Times", 15),fg='white',bg="#2E1114").place(x=1,y=60) 
    Label(window2,text="a) Between 10,000 and 50,000\n b) Between 50,000 and 150000\n c) Between 150000 and 500000\n   d) Between 500000 and 5000000",font=("Times", 15),fg='white',bg="#2E1114").place(x=5,y=90) 
    Label(window2,text="   e) More than 5000000",font=("Times", 15),fg='white',bg="#2E1114").place(x=5,y=182) 
    b2=Button(window2,text="Solution 2",font=("Times", 10),bd=5,command=sol2)
    b2.place(x=700, y=60)
    Label(window2,text="3) Which category of apps have managed to get the most,least and an average",font=("Times", 15),fg='white',bg="#2E1114").place(x=3,y=223) 
    Label(window2,text="   of 2,50,000 downloads atleast",font=("Times", 15),fg='white',bg="#2E1114").place(x=5,y=253) 
    b3=Button(window2,text="Solution 3",font=("Times", 10),bd=5,command=sol3)
    b3.place(x=700, y=223)
    Label(window2,text="4) Which category of apps have managed to get the highest maximum average.",font=("Times", 15),fg='white',bg="#2E1114").place(x=5,y=293) 
    Label(window2,text="   ratings from the users",font=("Times", 15),fg='white',bg="#2E1114").place(x=5,y=323) 
    b4=Button(window2,text="Solution 4",font=("Times", 10),bd=5,command=sol4)
    b4.place(x=700, y=293)
    Label(window2,text="5) What is the download trend category wise over the period for which",font=("Times", 15),fg='white',bg="#2E1114").place(x=5,y=363) 
    Label(window2,text="    the data is being made available.",font=("Times", 15),fg='white',bg="#2E1114").place(x=5,y=393) 
    b5=Button(window2,text="Solution 5",font=("Times", 10),bd=5,command=sol5)
    b5.place(x=700, y=363)
    extBtn1 = Button(window2, text='Q6-Q9',bg='#353b48', fg='white',command=next1).place(x=100, y=460)
    extBtn2 = Button(window2, text='Q10-Q14',bg='#353b48', fg='white',command=next2).place(x=180, y=460)
    extBtn3 = Button(window2, text='Q15-Q18',bg='#353b48', fg='white',command=next3).place(x=260, y=460)
    extBtn = Button(window2, text='Next >>>',bg='#5B8930', fg='white',command=next1).place(x=340, y=460)
    Label(window2, text="Consider 1,000+ downloads as 1 unit", font=("Open Sans", 9, 'italic'), fg='white',bg='#2E1114', anchor='w').place(x=550, y=460)
    window2.mainloop()

def next1():
    Label(window2, text="", bg='#2E1114',width='800', height='500').place(x=0, y=0)
    extBtn = Button(window2, text='Next >>>',bg='#5B8930', fg='white',command=next2).place(x=340, y=460)
    prevtBtn = Button(window2, text='<<< Prev',bg='#CF000F', fg='white',command=first).place(x=20, y=460) 
    extBtn1 = Button(window2, text='Q1-Q5',bg='#353b48', fg='white',command=first).place(x=100, y=460)
    extBtn2 = Button(window2, text='Q10-Q14',bg='#353b48', fg='white',command=next2).place(x=180, y=460)
    extBtn3 = Button(window2, text='Q15-Q18',bg='#353b48', fg='white',command=next3).place(x=260, y=460)
    Label(window2,text="6) For the years 2016,2017,2018 what are the category of apps that have got the most",font=("Times", 15),fg='white',bg="#2E1114").place(x=1,y=20) 
    Label(window2,text="    and the least downloads. What is the percentage increase or decrease that the",font=("Times", 15),fg='white',bg="#2E1114").place(x=5,y=50) 
    Label(window2,text="    apps have got over the period of three years.",font=("Times", 15),fg='white',bg="#2E1114").place(x=5,y=80) 
    b6=Button(window2,text="Solution 6",font=("Times", 10),bd=5,command=sol6)
    b6.place(x=700, y=20)
    Label(window2,text="7) All those apps , whose android version is not an issue and can work with varying ",font=("Times", 15),fg='white',bg="#2E1114").place(x=5,y=120) 
    Label(window2,text="     devices ,what is the percentage increase or decrease in the downloads",font=("Times", 15),fg='white',bg="#2E1114").place(x=5,y=150) 
    b7=Button(window2,text="Solution 7",font=("Times", 10),bd=5,command=sol7)
    b7.place(x=700, y=120)
    Label(window2,text="8) Amongst sports, entertainment,social media,news,events,travel and games,which",font=("Times", 15),fg='white',bg="#2E1114").place(x=5,y=190) 
    Label(window2,text="     is the category of app that is most likely to be downloaded in the coming years, ",font=("Times", 15),fg='white',bg="#2E1114").place(x=5,y=220) 
    Label(window2,text="     kindly make a prediction and back it with suitable findings.",font=("Times", 15),fg='white',bg="#2E1114").place(x=5,y=250) 
    b8=Button(window2,text="Solution 8",font=("Times", 10),bd=5)#,command=sol8
    b8.place(x=700, y=180)
    Label(window2,text="9) All those apps who habve managed to get over 1,00,000 downloads, have they",font=("Times", 15),fg='white',bg="#2E1114").place(x=5,y=290) 
    Label(window2,text="     managed to get an average rating of 4.1 and above? An we conclude something",font=("Times", 15),fg='white',bg="#2E1114").place(x=5,y=320) 
    Label(window2,text="     in co-relation to the number of downloads and the ratings received.",font=("Times", 15),fg='white',bg="#2E1114").place(x=5,y=350) 
    b9=Button(window2,text="Solution 9",font=("Times", 10),bd=5,command=sol9)
    b9.place(x=700, y=290)
    Label(window2, text="Consider 1,000+ downloads as 1 unit", font=("Open Sans", 9, 'italic'), fg='white',bg='#2E1114', anchor='w').place(x=550, y=460)
    
def next2():
    Label(window2, text="", bg='#2E1114',width='800', height='500').place(x=0, y=0)
    extBtn = Button(window2, text='Next >>>',bg='#5B8930', fg='white',command=next3).place(x=340, y=460)
    prevtBtn = Button(window2, text='<<< Prev',bg='#CF000F', fg='white',command=next1).place(x=20, y=460) 
    extBtn1 = Button(window2, text='Q1-Q5',bg='#353b48', fg='white',command=first).place(x=100, y=460)
    extBtn2 = Button(window2, text='Q6-Q9',bg='#353b48', fg='white',command=next1).place(x=180, y=460)
    extBtn3 = Button(window2, text='Q15-Q18',bg='#353b48', fg='white',command=next3).place(x=260, y=460)
    Label(window2,text="10) Across all the years ,which month has seen the maximum downloads for each of",font=("Times", 15),fg='white',bg="#2E1114").place(x=1,y=20) 
    Label(window2,text="     the category. What is the ratio of downloads for the app that qualifies as ",font=("Times", 15),fg='white',bg="#2E1114").place(x=5,y=50) 
    Label(window2,text="     teen versus mature17+.",font=("Times", 15),fg='white',bg="#2E1114").place(x=5,y=80) 
    b10=Button(window2,text="Solution 10",font=("Times", 10),bd=5,command=sol10)
    b10.place(x=700, y=20)
    Label(window2,text="11) Which quarter of which year has generated the highest number of install for",font=("Times", 15),fg='white',bg="#2E1114").place(x=5,y=120) 
    Label(window2,text="      each app used in the study?",font=("Times", 15),fg='white',bg="#2E1114").place(x=5,y=150) 
    b11=Button(window2,text="Solution 11",font=("Times", 10),bd=5,command=sol11)
    b11.place(x=700, y=120)
    Label(window2,text="12) Which of all the apps given have managed to generate the most positive and ",font=("Times", 15),fg='white',bg="#2E1114").place(x=5,y=190) 
    Label(window2,text="       negative sentiments.Also figure out the app which has generated approximately",font=("Times", 15),fg='white',bg="#2E1114").place(x=5,y=220) 
    Label(window2,text="       the same ratio for positive and negative sentiments.",font=("Times", 15),fg='white',bg="#2E1114").place(x=5,y=250) 
    b12=Button(window2,text="Solution 12",font=("Times", 10),bd=5,command=sol12)
    b12.place(x=700, y=180)
    Label(window2,text="13) Study and find out the relation between the Sentiment-polarity and sentiment-",font=("Times", 15),fg='white',bg="#2E1114").place(x=5,y=290) 
    Label(window2,text="     subjectivity of all the apps",font=("Times", 15),fg='white',bg="#2E1114").place(x=5,y=320) 
    b13=Button(window2,text="Solution 13",font=("Times", 10),bd=5,command=sol13)
    b13.place(x=700, y=290)
    Label(window2,text="14) Generate an interface where the client can see the reviews categorized as",font=("Times", 15),fg='white',bg="#2E1114").place(x=5,y=360) 
    Label(window2,text="     positive.negative and neutral ,once they have selected the app from a",font=("Times", 15),fg='white',bg="#2E1114").place(x=5,y=390) 
    Label(window2,text="      list of apps available for the study.",font=("Times", 15),fg='white',bg="#2E1114").place(x=5,y=420) 
    b14=Button(window2,text="Solution 14",font=("Times", 10),bd=5,command=sol14)
    b14.place(x=700, y=360)
    Label(window2, text="Consider 1,000+ downloads as 1 unit", font=("Open Sans", 9, 'italic'), fg='white',bg='#2E1114', anchor='w').place(x=550, y=460)
        
def next3():
    Label(window2, text="", bg='#2E1114',width='800', height='500').place(x=0, y=0)
    prevtBtn = Button(window2, text='<<< Prev',bg='#CF000F', fg='white',command=next2).place(x=20, y=460) 
    extBtn1 = Button(window2, text='Q1-Q5',bg='#353b48', fg='white',command=first).place(x=100, y=460)
    extBtn2 = Button(window2, text='Q6-Q9',bg='#353b48', fg='white',command=next1).place(x=180, y=460)
    extBtn2 = Button(window2, text='Q10-Q14',bg='#353b48', fg='white',command=next2).place(x=260, y=460)
    Label(window2,text="15) Is it advisable to launch an app like ’10 Best foods for you’? Do the users",font=("Times", 15),fg='white',bg="#2E1114").place(x=1,y=20) 
    Label(window2,text="     like these apps?",font=("Times", 15),fg='white',bg="#2E1114").place(x=5,y=50) 
    b15=Button(window2,text="Solution 15",font=("Times", 10),bd=5,command=sol15)
    b15.place(x=700, y=20)
    Label(window2,text="16) Which month(s) of the year , is the best indicator to the avarage downloads",font=("Times", 15),fg='white',bg="#2E1114").place(x=1,y=90) 
    Label(window2,text="       that an app will generate over the entire year?",font=("Times", 15),fg='white',bg="#2E1114").place(x=5,y=120) 
    b16=Button(window2,text="Solution 16",font=("Times", 10),bd=5,command=sol16)
    b16.place(x=700, y=90)
    Label(window2,text="17) Does the size of the App influence the number of installs  that it gets? if,yes ",font=("Times", 15),fg='white',bg="#2E1114").place(x=1,y=160) 
    Label(window2,text="       the trend is positive or negative with the increase in the app size",font=("Times", 15),fg='white',bg="#2E1114").place(x=5,y=190) 
    b17=Button(window2,text="Solution 17",font=("Times", 10),bd=5,command=sol17)
    b17.place(x=700, y=160)
    Label(window2,text="18) Provide an interface to add new data to both the datasets provided.",font=("Times", 15),fg='white',bg="#2E1114").place(x=1,y=220) 
    b18=Button(window2,text="Solution 18",font=("Times", 10),bd=5,command=Add_Data)
    b18.place(x=700, y=220)
    Label(window2, text="Additional Features:", font=("Times", 15), fg='#fbc531',bg='#2E1114', anchor='w').place(x=1, y=280)
    Label(window2, text="1. Download trend of all the categories for the desired year", font=("Times", 15), fg='white',bg='#2E1114', anchor='w').place(x=1, y=320)
    Label(window2, text="2. Check if your phones Andriod Versioin is compatiable or not", font=("Times", 15), fg='white',bg='#2E1114', anchor='w').place(x=1, y=360)
    b19=Button(window2,text="Solution",font=("Times", 10),bd=5, command=add1)
    b19.place(x=700, y=320)
    b20=Button(window2,text="Solution",font=("Times", 10),bd=5, command=and_ver)
    b20.place(x=700, y=365)
    Label(window2, text="Consider 1,000+ downloads as 1 unit", font=("Open Sans", 9, 'italic'), fg='white',bg='#2E1114', anchor='w').place(x=550, y=460)
    
def Add_Data12(c):
    if c.get()=="APP-DATA":
        Label(window6, text="", bg='#2E1114',width='70', height='25').place(x=45, y=170)   
        Label(window6, text="Add Data Excel Sheet", width='55', height="2", font=("Calibri", 22,'bold'), fg='white', bg='#FFB61E').place(x=0, y=40)
        Label(window6, text="", bg='#2E1114', width='90', height='20').place(x=45, y=120)
        
        Label(window6, text="App Name:", font=("Open Sans", 11, 'bold'), fg='white',bg='#2E1114', anchor='w').place(x=50, y=130)
        Entry(window6, textvar=app_name).place(x=150, y=130)

        Label(window6, text="Category:", font=("Open Sans", 11, 'bold'), fg='white',bg='#2E1114', anchor='w').place(x=50, y=180)
        Entry(window6, textvar=category).place(x=150, y=180)
        
        Label(window6, text="Rating:", font=("Open Sans", 11, 'bold'), fg='white', bg='#2E1114', anchor='w').place(x=50, y=230)
        Entry(window6, textvar=rating).place(x=150, y=230)
        
        Label(window6, text="Review:", font=("Open Sans", 11, 'bold'), fg='white', bg='#2E1114', anchor='w').place(x=50, y=280)
        Entry(window6, textvar=reviews).place(x=150, y=280)
        
        Label(window6, text="Size:", font=("Open Sans", 11, 'bold'), fg='white', bg='#2E1114', anchor='w').place(x=50, y=330)
        Entry(window6, textvar=size).place(x=150, y=330)
         
        Label(window6, text="Installs:", font=("Open Sans", 11, 'bold'), fg='white', bg='#2E1114', anchor='w').place(x=50, y=380)
        Entry(window6, textvar=installs).place(x=150, y=380)
        
        Label(window6, text="Type:", font=("Open Sans", 11, 'bold'), fg='white', bg='#2E1114', anchor='w').place(x=50, y=430)
        Entry(window6, textvar=typee).place(x=150, y=430)
        
        Label(window6, text="Price:", font=("Open Sans", 11, 'bold'), fg='white', bg='#2E1114', anchor='w').place(x=400, y=130)
        Entry(window6, textvar=price).place(x=550, y=130)
        
        Label(window6, text="Content Rating:", font=("Open Sans", 11, 'bold'), fg='white', bg='#2E1114', anchor='w').place(x=400, y=180)
        Entry(window6, textvar=cont_rating).place(x=550, y=180)
    
        Label(window6, text="Genre:", font=("Open Sans", 11, 'bold'), fg='white', bg='#2E1114', anchor='w').place(x=400, y=230)
        Entry(window6, textvar=genre).place(x=550, y=230)
        
        Label(window6, text="Last Updated:", font=("Open Sans", 11, 'bold'), fg='white', bg='#2E1114', anchor='w').place(x=400, y=280)
        Entry(window6, textvar=last_up).place(x=550, y=280)
        
        Label(window6, text="Current Version:", font=("Open Sans", 11, 'bold'), fg='white', bg='#2E1114', anchor='w').place(x=400, y=330)
        Entry(window6, textvar=cur_ver).place(x=550, y=330)
        
        Label(window6, text="Android Version:", font=("Open Sans", 11, 'bold'), fg='white', bg='#2E1114', anchor='w').place(x=400, y=380)
        Entry(window6, textvar=and_ver).place(x=550, y=380)
    
        Button(window6, text='Submit', width=20, font=("Open Sans", 13, 'bold'), bg='#FFB61E',fg='white',command=submit_data1).place(x=400, y=430)
    else:
       Label(window6, text="", bg='#2E1114', width='100', height='50').place(x=0, y=100)
       Label(window6, text="User Review Excel Sheet ", width='55', height="2", font=("Calibri", 22,'bold'), fg='white', bg='#FFB61E').place(x=0, y=40)
         
       Label(window6, text="App Name:", font=("Open Sans", 11, 'bold'), fg='white',bg='#2E1114', anchor='w').place(x=50, y=130)
       Entry(window6, textvar=app_name).place(x=150, y=130)
        
       Label(window6, text="Review", font=("Open Sans", 11, 'bold'), fg='white',bg='#2E1114', anchor='w').place(x=50, y=180)
       Entry(window6, textvar=reviews).place(x=150, y=180)
       
       Label(window6, text=" Add reviews of same app in sequence", font=("Open Sans", 11, 'italic'), fg='white',bg='#2E1114', anchor='w').place(x=400, y=130)
       Button(window6, text='Submit', width=20, font=("Open Sans", 13, 'bold'), bg='#FFB61E',fg='white',command=submit_data2).place(x=250, y=430)
             
def Add_Data():
    global window6, app_name, category, rating, reviews, size, installs, typee, price, cont_rating, genre, last_up, cur_ver, and_ver 
    choice=StringVar()
    app_name = StringVar()
    category = StringVar()
    rating = StringVar()
    reviews = StringVar()
    size = StringVar()
    installs = StringVar()
    typee = StringVar()
    price = StringVar()
    cont_rating = StringVar()
    genre = StringVar()
    last_up = StringVar()
    cur_ver = StringVar()
    and_ver = StringVar()
    window6 = Toplevel(window2)
    window6.title("Add Data")
    adjustWindow(window6) # configuring the window
    Label(window6, text="Select destination to add data", font=("Open Sans", 12, 'bold'), fg='white',bg='#2E1114').grid(row=2,column=0, pady=(5,0))
    list1 = ["APP-DATA","USER_REVIEWS"]
    droplist = OptionMenu(window6, choice, *list1, command=lambda x:Add_Data12(choice))
    choice.set('--Select--')
    droplist.config(width=25)
    droplist.grid(row=2, column=1, pady=(5,0))

def submit_data1():
    st=[]
    if app_name.get() and category.get() and rating.get() and reviews.get() and size.get() and installs.get() and typee.get() and price.get() and cont_rating.get() and genre.get and last_up.get() and cur_ver.get() and and_ver.get(): # checking for all empty values in entry field
        st.append(app_name.get())
        st.append(category.get())
        if rating.get()=='Nan':
            st.append(rating.get())
        else:
            st.append(float(rating.get()))
        st.append(reviews.get())
        st.append(size.get())
        st.append(installs.get())
        st.append(typee.get())
        st.append(price.get())
        st.append(cont_rating.get())
        st.append(genre.get())
        st.append(last_up.get())
        if cur_ver.get()=='Varies with device':
            st.append(cur_ver.get())
        else:
            st.append(float(cur_ver.get()))
        st.append(and_ver.get())
        s=add_data(st)
        messagebox.showinfo("Analysis",'\n'.join(s),parent=window6)    
    else:
        messagebox.showerror("Error","Please fill all the details",parent=window6)
        return
    
def submit_data2():
    strr={}
    if app_name.get() and reviews.get():
        strr.update({app_name.get():reviews.get()})
        s=user_review(strr)
        messagebox.showinfo("Analysis",',\n'.join(s),parent=window6)    
    else:
        messagebox.showerror("Error","Please fill all the details",parent=window6)
mainscreen()
