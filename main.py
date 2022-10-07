from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import ast
from minimal_login import *

w=Tk()
w.geometry('925x500')
w.title('Login')
w.configure(bg='#ff4f5a')
w.minsize(925,500)
    
signin()
signup()   
    
q.mainloop()