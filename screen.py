from tkinter import*
from tkinter import Tk,messagebox,StringVar,IntVar,Label,Radiobutton,Entry,Checkbutton,Button,OptionMenu,Toplevel,Message,PhotoImage
#from secpg import second_page 


def adjustWindow(window):
     w = 800 # width for the window size
     h = 500 # height for the window size
     ws = root.winfo_screenwidth() # width of the screen
     hs = root.winfo_screenheight() # height of the screen
     x = (ws/2) - (w/2) # calculate x and y coordinates for the Tk window
     y = (hs/2) - (h/2)
     window.geometry('%dx%d+%d+%d' % (w, h, x, y)) # set the dimensions of the screen
     #and where it is placed
     window.resizable(False, False) # disabling the resize option for the window
     window.configure(background='#174873') # making the bacgrd white in the window
     # validate the entry data and makes a new entry into the database




def mainscreen():
    global root
    root=Tk()
    adjustWindow(root)
    root.title("Google PlayStore App Launch Study")
    photo = PhotoImage(file="E:\\python\\project\\m88.png")
    label = Label(root,image=photo,text="")
    label.pack()
    label.image=photo
    Button(root, text="Proceed", bg="#e79700", width=20, height=2, font=("Open Sans",13, 'bold'), fg='white',command=second_page).place(x=100, y=300)
    
    root.mainloop()
        

def second_page(): 
    global window
    window = Toplevel(root)
    window.title("Welcome")
    adjustWindow(window) # 
    #window.configure(bg="#999999")
    #window.title("BROCODE")
    
    photo = PhotoImage(file="E:\\python\\project\\2nd_page.png")
    label = Label(window,image=photo,text="")
    label.place(x=0,y=0)
    label.image=photo
    
    lbl = Label(window, text="Select a category:", font=("Times", 30),bg="#999999" )
    lbl.grid(column=1, row=0, padx=10,columnspan=3, pady=10,ipadx=20)
                
    btn = Button(window, text="Download", height = 2, width = 9)#command=third_page
    btn.grid(column=2, row=3, padx=20, pady=10,ipadx=20)

    btn = Button(window, text="Sentiment Analysis", height = 2, width = 9)
    btn.grid(column=2, row=6, padx=20, pady=10,ipadx=20)

    btn = Button(window, text="Prediction", height = 2, width = 9)
    btn.grid(column=3, row=3, padx=15,  pady=10,ipadx=20)

    btn = Button(window, text="More", height = 2, width = 9)
    btn.grid(column=3, row=6,padx=15, pady=10,ipadx=20)

    btn = Button(window, text="Add Data", height = 2, width = 6)
    btn.grid(column=2, row=8,columnspan=2, pady=10,ipadx=20)


    #window.mainloop()
"""
def sec_page():
    global screen1
    screen1 = Toplevel(root)
    screen1.title("Google PlayStore App Launch Study")
    adjustWindow(screen1) # configuring the window
    screen1.configure(background='#999999')
    Label(screen1, text="select a category", width='40', height="2", font=("Calibri", 22,'bold'), fg='white', bg='#999999').place(x=0, y=0)
    Button(screen1, text='', width=20, font=("Open Sans", 13, 'bold'), bg='brown',fg='white').place(x=150, y=160)
    Button(screen1, text='Submit', width=20, font=("Open Sans", 13, 'bold'), bg='brown',fg='white').place(x=150, y=160)
"""




#    ent = Entry(root)
#    ent.pack()
#    ent.focus_set() 
#    
    
#def sec_page():
##    global screen1
##    screen1 = Toplevel(root)
##    screen1.title("Google PlayStore App Launch Study")
##    adjustWindow(screen1) # configuring the window
##    screen1.configure(background='#999999')
##    photo2 = PhotoImage(file="sec.jpg")
##    label = Label(root,image=photo2,text="")
##    label.pack()
##    label.image=photo2
#    
#    adjustWindow(root)
#    
#    photo = PhotoImage(file = "lol.png")
#    w = Label(root, image=photo)
#    w.pack()
#    root.configure(bg=w)
#   
#    root.mainloop()
#    
mainscreen()
c