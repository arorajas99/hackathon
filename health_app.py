from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import ast
import webbrowser
from twilio.rest import Client

w=Toplevel()
w.geometry('900x500')
w.configure(bg='#262626')#12c4c0')
w.resizable(0,0)
w.title('Toggle Menu')

def registration():
    def main():
        win = Tk()
        win.geometry('350x350')
        win.title('Book an appointment')
        button = Button(win, text='Book an appointment',command=book)
        button.place(x=100,y=80)
        button.config(height=5,width=20)
        button.pack()
        win.configure(bg='pink')
        button2 = Button(win, text='Cancel an appointment',command=cancel)
        button2.place(x=100,y=200)
        button2.config(height=5, width=20)
        button2.pack()
        button3 = Button(win, text='View an appointment',command=view)
        button3.place(x=100,y=300)
        button3.config(height=5, width=20)
        button3.pack()
        win.mainloop()
    
    def cancel():
        message = "Appointment has been cancelled"
    
    
    def view():
        print("view")
    
    
    def message():
        a = 1
        account_sid = 'ACb789fb03c14205987d7c88ca0eadf209'
        auth_token = '803ca069c1bcefb9530d98b5f8a6760f'
        client = Client(account_sid, auth_token)
    
        message = client.messages \
            .create(
            body="Your appointment has been booked. Patient Name = {} and Phone Number = {} Your booking number is {}".format(
                entry1.get(), entry2.get(), a),
            from_='+18782177081',
            to='+91{}'.format(entry2.get())
    
        )
        a = a + 1
    
    def book():
        win = Tk()
        win.geometry('500x500')
        label1 = Label(win, text='Enter your Name')
        label1.pack()
        global entry1
        entry1 = Entry(win)
        entry1.pack()
        label2 = Label(win, text='Enter your Phone Number ')
        label2.pack()
        global entry2
        entry2 = Entry(win)
        entry2.pack()
        drop = OptionMenu(win, "Select ", "Fever", "Cold", "Cough", "Headache", "Stomachache", "Others")
        drop.pack()
        button = Button(win, text="SUBMIT",command = message)
        button.pack()
        # x = drop()
        # print(x)
    
    main()


def advice():
    w = Tk()
    w.geometry('250x250')
    w.title('')

    def open():
        webbrowser.open('https://main.mohfw.gov.in/department-health-and-family-welfare-directory')
        
    button1 = Button(w,width=20,font=('arial',15),text='Advisory',command=open)
    button1.place(x=10,y=100)
    w.mainloop()
    



def registration2():
    w=Toplevel()
    w.geometry('925x500')
    w.title('Login')
    w.configure(bg='#ff4f5a')
    w.minsize(925,500)
    
    
    def signin():
        signin_win=Frame(w,width=925,height=500,bg='white')
        signin_win.place(x=0,y=0)
        f1=Frame(signin_win,width=350,height=350,bg='white')
        f1.place(x=480,y=100)
        
        global img1
        img1 = ImageTk.PhotoImage(Image.open("signin.png"))
        Label(signin_win,image=img1,border=0,bg='white').place(x=50,y=50)
    
        l2=Label(signin_win,text="Book an appointment",fg='#ff4f5a',bg='white')
        l2.config(font=('Microsoft YaHei UI Light',23, 'bold'))
        l2.place(x=500,y=60)
    
        def on_enter(e):
            e1.delete(0,'end')    
        def on_leave(e):
            if e1.get()=='':   
                e1.insert(0,'Username')
    
        
        e1 =Entry(f1,width=25,fg='black',border=0,bg='white')
        e1.config(font=('Microsoft YaHei UI Light',11, ))
        e1.bind("<FocusIn>", on_enter)
        e1.bind("<FocusOut>", on_leave)
        e1.insert(0,'Username')
        e1.place(x=30,y=60)    
        Frame(f1,width=295,height=2,bg='black').place(x=25,y=87)
    
        #------------------------------------------------------
    
        def on_enter(e):
            e2.delete(0,'end')    
        def on_leave(e):
            if e2.get()=='':   
                e2.insert(0,'Phone number')
    
        
        e2 =Entry(f1,width=21,fg='black',border=0,bg='white')
        e2.config(font=('Microsoft YaHei UI Light',11, ))
        e2.bind("<FocusIn>", on_enter)
        e2.bind("<FocusOut>", on_leave)
        e2.insert(0,'Password')
        e2.place(x=30,y=130)
    
        Frame(f1,width=295,height=2,bg='black').place(x=25,y=157)
    
        #-mech------------------------------------------------
        def signin_cmd():
            
            file=open('datasheet.txt','r')
            d=file.read()
            r=ast.literal_eval(d)
            file.close()
            
    
            key=e1.get()
            value=e2.get()
            
            if key in r.keys() and value==r[key]:           
                messagebox.showinfo("","     successfully logged in    ")
                w.destroy()
                import main
            else:
                messagebox.showwarning('try again', 'invalid username or password')
    
    
        #------------------------------------------------------
        Button(f1,width=39,pady=7,text='Book',bg='#ff4f5a',fg='white',border=0,command=signin_cmd).place(x=35,y=204)
        l1=Label(f1,text="Don't have an account?",fg="black",bg='white')
        l1.config(font=('Microsoft YaHei UI Light',9, ))
        l1.place(x=75,y=250)
    
        b2=Button(f1,width=6,text='Sign up',border=0,bg='white',fg='#ff4f5a',command=signup)
        b2.place(x=215,y=250)
    
    
    
    
    def signup():
        signup_win=Frame(w,width=925,height=500,bg='white')
        signup_win.place(x=0,y=0)
        f1=Frame(signup_win,width=350,height=350,bg='white')
        f1.place(x=480,y=70)
    
        
        global img2
        img2 = ImageTk.PhotoImage(Image.open("signup.png"))
        Label(signup_win,image=img2,border=0,bg='white').place(x=30,y=90)
    
        l2=Label(signup_win,text="Sign up",fg='#ff4f5a',bg='white')
        l2.config(font=('Microsoft YaHei UI Light',23, 'bold'))
        l2.place(x=600,y=60)
    
        def on_enter(e):
            e1.delete(0,'end')    
        def on_leave(e):
            if e1.get()=='':   
                e1.insert(0,'Username')
    
        
        e1 =Entry(f1,width=25,fg='black',border=0,bg='white')
        e1.config(font=('Microsoft YaHei UI Light',11, ))
        e1.bind("<FocusIn>", on_enter)
        e1.bind("<FocusOut>", on_leave)
        e1.insert(0,'Username')
        e1.place(x=30,y=60)
    
        Frame(f1,width=295,height=2,bg='black').place(x=25,y=87)
    
        #------------------------------------------------------
    
        def on_enter(e):
            e2.delete(0,'end')    
        def on_leave(e):
            if e2.get()=='':   
                e2.insert(0,'Password')
    
        
        e2 =Entry(f1,width=21,fg='black',border=0,bg='white')
        e2.config(font=('Microsoft YaHei UI Light',11, ))
        e2.bind("<FocusIn>", on_enter)
        e2.bind("<FocusOut>", on_leave)
        e2.insert(0,'Password')
        e2.place(x=30,y=130)
    
        Frame(f1,width=295,height=2,bg='black').place(x=25,y=157)
    
        def on_enter(e):
            e3.delete(0,'end')    
        def on_leave(e):
            if e3.get()=='':   
                e3.insert(0,'Phone number')
    
        
        e3 =Entry(f1,width=21,fg='black',border=0,bg='white')
        e3.config(font=('Microsoft YaHei UI Light',11, ))
        e3.bind("<FocusIn>", on_enter)
        e3.bind("<FocusOut>", on_leave)
        e3.insert(0,'Phone number')
        e3.place(x=30,y=130+70)
    
        Frame(f1,width=295,height=2,bg='black').place(x=25,y=157+70)    
    
        
        #Mechenism------------------------------------------------
        
        def signup_cmd():
            key=e1.get()
            value=e2.get()
            value2=e3.get()
            
            if value==value2:
                file=open('datasheet.txt','r+')
                d=file.read()
                r=ast.literal_eval(d)
                print(r)
                
    
                dict2={key:value}
                print(dict2)
                r.update(dict2)
                print(r)
                file.truncate(0)
                file.close()
                print(r)
                file=open('datasheet.txt','w')
                w=file.write(str(r))
                 
                messagebox.showinfo("","     successfully signed up     ")
                
            else:
                messagebox.showwarning('try again', 'password should match ')
    
    
        #-------------------------------------------------------
        Button(f1,width=38,pady=7,text='Sign up',bg='#ff4f5a',fg='white',border=0,command=signup_cmd).place(x=35,y=204+60)
        l1=Label(f1,text="Already have an account?",fg="black",bg='white')
        l1.config(font=('Microsoft YaHei UI Light',9, ))
        l1.place(x=60,y=250+63)
    
        b2=Button(f1,width=25,text='Book an appointment',border=0,bg='white',fg='#ff4f5a',command=signin)
        b2.place(x=200,y=250+63)
    
    signin() #default screen
    
    w.mainloop()



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
 

def appointment():
    f1.destroy()
    registration()
    toggle_win()
   
    

def advisory():
    f1.destroy()
    f2=Frame(w,width=900,height=455,bg='white')
    f2.place(x=0,y=45)
    l2=Label(f2,text='advisory',fg='black',bg='white')
    l2.config(font=('Comic Sans MS',90))
    l2.place(x=320,y=150-45)
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
    bttn(0,240,'Goverment Advisory','#0f9d9a','#12c4c0',advice)
    bttn(0,160,'BOOK AN APPOINTMENT','#0f9d9a','#12c4c0',registration2)
    bttn(0,320,'EMERGENCY','#0f9d9a','#12c4c0',None)
    
    


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
