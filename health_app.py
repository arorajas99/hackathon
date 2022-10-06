#importing library
from tkinter import *
from tkinter import font
from PIL import ImageTk, Image 
import time


def main_program():
    w=Toplevel()
    w.geometry('900x500')
    w.configure(bg='#262626')#12c4c0')
    w.resizable(0,0)
    w.title('Toggle Menu')
    
    
    def default_home():
        f2=Frame(w,width=900,height=455,bg='#262626')
        f2.place(x=0,y=45)
        l2=Label(f2,text='Home',fg='white',bg='#262626')
        l2.config(font=('Comic Sans MS',90))
        l2.place(x=290,y=150-45)
    
       
    def home():
        f1.destroy()
        f2=Frame(w,width=900,height=455,bg='#262626')
        f2.place(x=0,y=45)
        l2=Label(f2,text='Home',fg='white',bg='#262626')
        l2.config(font=('Comic Sans MS',90))
        l2.place(x=290,y=150-45)
        toggle_win()
     
    
    def login():
        f1.destroy()
        window = Tk()
        window.title('SignUp')
        window.geometry('900x455')
        window.configure(bg='#fff')
        window.resizable(False,False)
        img = PhotoImage(file='login.png')
        Label(window,image=img,border=0,bg='white').place(x=50,y=90)
        
        frame = Frame(window,width=350,height=390,bg='red')
        frame.place(x=480,y=50)
        
        heading = Label(frame,text='Sign Up',fg='#57a1f8',bg='white',font=("Microsoft Yahei UI Light",23,'bold'))
        heading.place(x=100,y=5)
        
        # entry
        user = Entry(frame,width=25,fg='black',border=2,bg='white',font=('Microsoft Yahei UI Light',11))
        user.place(x=30,y=80)
        user.insert(0,'Username')
        Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)
        toggle_win()
        
        

       
        

    
    
    def toggle_win():
        global f1
        f1=Frame(w,width=300,height=500,bg='#12c4c0')
        f1.place(x=0,y=0)
        
        #buttons
        def bttn(x,y,text,bcolor,fcolor,cmd):
         
            def on_entera(e):
                myButton1['background'] = bcolor #ffcc66
                myButton1['foreground']= '#262626'  #000d33
    
            def on_leavea(e):
                myButton1['background'] = fcolor
                myButton1['foreground']= '#262626'
    
            myButton1 = Button(f1,text=text,
                           width=42,
                           height=2,
                           fg='#262626',
                           border=0,
                           bg=fcolor,
                           activeforeground='#262626',
                           activebackground=bcolor,            
                            command=cmd)
                          
            myButton1.bind("<Enter>", on_entera)
            myButton1.bind("<Leave>", on_leavea)
    
            myButton1.place(x=x,y=y)
    
        bttn(0,80,'H O M E','#0f9d9a','#12c4c0',home)
        bttn(0,160,'L O G I N / S I G N U P','#0f9d9a','#12c4c0',login)
        bttn(0,240,'A D V I S O R Y','#0f9d9a','#12c4c0',None)
        bttn(0,320,'E M E R G E N C Y','#0f9d9a','#12c4c0',None)
    
        #
        def dele():
            f1.destroy()
            b2=Button(w,image=img1,
                   command=toggle_win,
                   border=0,
                   bg='#262626',
                   activebackground='#262626')
            b2.place(x=5,y=8)
    
        global img2
        img2 = ImageTk.PhotoImage(Image.open("close.png"))
    
        Button(f1,
               image=img2,
               border=0,
               command=dele,
               bg='#12c4c0',
               activebackground='#12c4c0').place(x=5,y=10)
        
    
    default_home()
    
    img1 = ImageTk.PhotoImage(Image.open("open.png"))
    
    global b2
    b2=Button(w,image=img1,
           command=toggle_win,
           border=0,
           bg='#262626',
           activebackground='#262626')
    b2.place(x=5,y=8)
    
    
    w.mainloop()


def screen():

    w=Toplevel()
    
    #Using piece of code from old splash screen
    width_of_window = 427
    height_of_window = 250
    screen_width = w.winfo_screenwidth()
    screen_height = w.winfo_screenheight()
    x_coordinate = (screen_width/2)-(width_of_window/2)
    y_coordinate = (screen_height/2)-(height_of_window/2)
    w.geometry("%dx%d+%d+%d" %(width_of_window,height_of_window,x_coordinate,y_coordinate))
    #w.configure(bg='#ED1B76')
    w.overrideredirect(1) #for hiding titlebar
    
    #new window to open
    def new_win():
        q=Tk()
        main_program()
        q.mainloop()
    
    Frame(w, width=427, height=250, bg='#272727').place(x=0,y=0)
    label1=Label(w, text='MediCare', fg='white', bg='#272727') #decorate it 
    label1.configure(font=("Game Of Squids", 24, "bold"))   #You need to install this font in your PC or try another one
    label1.place(x=80,y=90)
    
    label2=Label(w, text='Loading...', fg='white', bg='#272727') #decorate it 
    label2.configure(font=("Calibri", 11))
    label2.place(x=10,y=215)
    
    #making animation
    
    image_a=ImageTk.PhotoImage(Image.open('c2.png'))
    image_b=ImageTk.PhotoImage(Image.open('c1.png'))
    
    
    
    
    for i in range(3): #3loops
        l1=Label(w, image=image_a, border=0, relief=SUNKEN).place(x=180, y=145)
        l2=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=200, y=145)
        l3=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=220, y=145)
        l4=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=240, y=145)
        w.update_idletasks()
        time.sleep(0.5)
    
        l1=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=180, y=145)
        l2=Label(w, image=image_a, border=0, relief=SUNKEN).place(x=200, y=145)
        l3=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=220, y=145)
        l4=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=240, y=145)
        w.update_idletasks()
        time.sleep(0.5)
    
        l1=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=180, y=145)
        l2=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=200, y=145)
        l3=Label(w, image=image_a, border=0, relief=SUNKEN).place(x=220, y=145)
        l4=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=240, y=145)
        w.update_idletasks()
        time.sleep(0.5)
    
        l1=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=180, y=145)
        l2=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=200, y=145)
        l3=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=220, y=145)
        l4=Label(w, image=image_a, border=0, relief=SUNKEN).place(x=240, y=145)
        w.update_idletasks()
        time.sleep(0.5)
    
    
    
    w.destroy()
    new_win()
    
screen()
