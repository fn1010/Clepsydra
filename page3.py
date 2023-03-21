from tkinter import *
import datetime
import time
from playsound import playsound
from threading import *
from tkinter import messagebox
from PIL import ImageTk, Image

ws = Tk()
ws.geometry('1400x600')
ws.title('Clepsydra-timer')
ws['bg']='purple'

f = ("Times bold", 14)

Label(ws,text="Set Timer",font=("Helvetica 15 bold")).pack(pady=10)
hour1=StringVar()
minute1=StringVar()
second1=StringVar()
  
# setting the default value as 0
hour1.set("00")
minute1.set("00")
second1.set("00")

# Use of Entry class to take input from the user
hourEntry= Entry(ws, width=3, font=("Arial",18,""),
                 textvariable=hour1)
hourEntry.place(x=630,y=50)
 
minuteEntry= Entry(ws, width=3, font=("Arial",18,""),
                   textvariable=minute1)
minuteEntry.place(x=680,y=50)
  
secondEntry= Entry(ws, width=3, font=("Arial",18,""),
                   textvariable=second1)
secondEntry.place(x=730,y=50)
  

def submit():
    try:
        # the input provided by the user is
        # stored in here :temp
        temp = int(hour1.get())*3600 + int(minute1.get())*60 + int(second1.get())
    except:
        print("Please input the right value")
    while temp >-1:
         
        # divmod(firstvalue = temp//60, secondvalue = temp%60)
        mins,secs = divmod(temp,60)
  
        # Converting the input entered in mins or secs to hours,
        # mins ,secs(input = 110 min --> 120*60 = 6600 => 1hr :
        # 50min: 0sec)
        hours=0
        if mins >60:
             
            # divmod(firstvalue = temp//60, secondvalue
            # = temp%60)
            hours, mins = divmod(mins, 60)
         
        # using format () method to store the value up to
        # two decimal places
        hour1.set("{0:2d}".format(hours))
        minute1.set("{0:2d}".format(mins))
        second1.set("{0:2d}".format(secs))
  
        # updating the GUI window after decrementing the
        # temp value every time
        ws.update()
        time.sleep(1)
  
        # when temp value = 0; then a messagebox pop's up
        # with a message:"Time's up"
        if (temp == 0):
            playsound('mixkit-fast-rocket-whoosh-1714.wav')
            messagebox.showinfo("Time Countdown", "Time's up ")
         
        # after every one sec the value of temp will be decremented
        # by one
        temp -= 1
 
# button widget
btn = Button(ws, text='Set Time Countdown', bd='5',
             command= submit).pack(pady=40)

def nextPage1():
    ws.destroy()
    import page4

def nextPage():
    ws.destroy()
    import page1

def prevPage():
    ws.destroy()
    import page2

frame = Frame(ws,)
frame.pack()

# Create an object of tkinter ImageTk

img = ImageTk.PhotoImage(Image.open("timer.jpg"))

# Create a Label Widget to display the text or Image
label = Label(frame, image = img)
label.pack()
    
Label(
    ws,
    text="Timer figure",
    font = f,
    padx=20,
    pady=20,
    bg='purple',
    fg='white'
).pack(expand=True, fill=BOTH)

Button(
    ws, 
    text="Back to Alarm", 
    font=f,
    command=prevPage,
    background='yellow'
    ).pack(fill=X, expand=TRUE, side=LEFT)

Button(
    ws, 
    text="Back to Clepsydra",
    font = f,
    command=nextPage,
    background='yellow'
    ).pack(fill=X, expand=TRUE, side=LEFT)
Button(
    ws, 
    text=" Next Stopwatch", 
    font=f,
    command=nextPage1,
    background='yellow'
    ).pack(fill=X, expand=TRUE, side=LEFT)

ws.mainloop()