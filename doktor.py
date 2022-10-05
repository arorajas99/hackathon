import tkinter as tk
from twilio.rest import Client


def main():
    win = tk.Tk()
    win.geometry('350x350')
    win.title('Book an appointment')
    button = tk.Button(win, text='Book an appointment',command=book)
    button.place(x=100,y=100)
    button.pack()
    win.configure(bg='pink')
    win.mainloop()


def message():
    a = 1
    account_sid = 'ACb789fb03c14205987d7c88ca0eadf209'
    auth_token = 'd8a6357f236c1bc660b9f5bfbbf56f1b'
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body="Your appointment has been booked. Patient Name = {} and Phone Number = {} Your booking number is {}".format(entry1.get(),entry2.get(),a) ,
        from_='+18782177081',
        to='+91{}'.format(entry2.get())
    )
    a = a+1

def book():
    win = tk.Tk()
    win.geometry('500x500')
    label1 = tk.Label(win, text='Enter your Name')
    label1.pack()
    global entry1
    entry1 = tk.Entry(win)
    entry1.pack()
    label2 = tk.Label(win, text='Enter your Phone Number ')
    label2.pack()
    global entry2
    entry2 = tk.Entry(win)
    entry2.pack()
    button = tk.Button(win, text="SUBMIT",command=message)
    button.pack()
main()