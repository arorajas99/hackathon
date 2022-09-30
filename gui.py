import tkinter as tk
import sqlite3
import bcrypt
con = sqlite3.connect('test1.db')
cur = con.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS test1(username TEXT ,password TEXT)''')
# login_username = []
# login_pass = []

#hashed = bcrypt.hashpw()


def add():

    win = tk.Tk()
    global a
    a = entry1.get()
    global b
    b = entry2.get()
    # login_username.append(a)
    # login_pass.append(b)
    cur.execute("SELECT COUNT(*) FROM test1 WHERE username = '" + a +"'")
    result = cur.fetchone()
    cur.execute("INSERT INTO test1 VALUES (?,?)",(a,b))


def true():
    win = tk.Tk()
    win.geometry('5000x5000')
    win.configure(bg='green')


def false():
    win = tk.Tk()
    win.geometry('5000x5000')
    win.configure(bg='red')


def main():
    win = tk.Tk()
    win.geometry('5000x5000')
    win.title('OUR APPLICATION')
    win.minsize(500, 500)
    win.maxsize(500, 500)
    win.configure(bg='#F1BBB0')
    btn1 = tk.Button(win, text='Sign In', bg='black', fg='white', font='Courier 15 bold italic', command=login)
    btn1.place(x=100, y=350)

    btn2 = tk.Button(win, text='Sign Up', bg='red', font='Courier 15 bold italic', command=signup)
    btn2.place(x=300, y=350)

    win.mainloop()


def login():
    win_login = tk.Tk()
    username = tk.StringVar()
    password = tk.StringVar()

    def check():
        
        x = field.get()
        x1 = field2.get()
        cur.execute("SELECT username,password FROM test1")
        rows = cur.fetchall()
        
        if (x,x1) in rows:
            val = 1
            true()
        else:
            false()


    win_login.geometry('500x500')
    win_login.title('TITLE')
    label = tk.Label(win_login, text='Username')
    label.pack()

    label2 = tk

    field = tk.Entry(win_login)
    field.pack()

    label3 = tk.Label(win_login, text='Password')
    label3.pack()

    field2 = tk.Entry(win_login, show="*")
    field2.pack()

    btn = tk.Button(win_login, text='Sign In', command=check)
    btn.pack()

    win_login.mainloop()


def signup():
    siup = tk.Tk()
    siup.geometry('500x500')
    label1 = tk.Label(siup, text='Enter your username')
    label1.pack()
    global entry1
    entry1 = tk.Entry(siup)
    entry1.pack()
    label2 = tk.Label(siup, text='Enter your password')
    label2.pack()
    global entry2
    entry2 = tk.Entry(siup)
    entry2.pack()
    button = tk.Button(siup, text="SUBMIT", command=add)
    button.pack()
    
    
con.commit()


main()