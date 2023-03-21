import tkinter as Tkinter
from datetime import datetime
from tkinter import *
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

frame = Frame(ws,)
frame.pack()

# Create an object of tkinter ImageTk

img = ImageTk.PhotoImage(Image.open("countdown.jpg"))

# Create a Label Widget to display the text or Image
label = Label(frame, image = img)
label.pack(padx=20)

counter = 66600
running = False
def counter_label(label):
    def count():
        if running:
            global counter
   
            # To manage the initial delay.
            if counter==66600:            
                display="Starting..."
            else:
                tt = datetime.fromtimestamp(counter)
                string = tt.strftime("%H:%M:%S")
                display=string
   
            label['text']=display   # Or label.config(text=display)
   
            # label.after(arg1, arg2) delays by 
            # first argument given in milliseconds
            # and then calls the function given as second argument.
            # Generally like here we need to call the 
            # function in which it is present repeatedly.
            # Delays by 1000ms=1 seconds and call count again.
            label.after(1000, count) 
            counter += 1
   
    # Triggering the start of the counter.
    count()     
   
# start function of the stopwatch
def Start(label):
    global running
    running=True
    counter_label(label)
    start['state']='disabled'
    stop['state']='normal'
    reset['state']='normal'
   
# Stop function of the stopwatch
def Stop():
    global running
    start['state']='normal'
    stop['state']='disabled'
    reset['state']='normal'
    running = False
   
# Reset function of the stopwatch
def Reset(label):
    global counter
    counter=66600
   
    # If rest is pressed after pressing stop.
    if running==False:      
        reset['state']='disabled'
        label['text']='Welcome!'
   
    # If reset is pressed while the stopwatch is running.
    else:               
        label['text']='Starting...'
   

   
# Fixing the window size.
label = Tkinter.Label(ws, text="Welcome!", fg="black", font="Verdana 30 bold")
label.pack(padx=20,pady=20)
f = Tkinter.Frame(ws)
start = Tkinter.Button(f, text='Start', width=6, command=lambda:Start(label))
stop = Tkinter.Button(f, text='Stop',width=6,state='disabled', command=Stop)
reset = Tkinter.Button(f, text='Reset',width=6, state='disabled', command=lambda:Reset(label))
f.pack(anchor = 'center',pady=5)
start.pack(side="left")
stop.pack(side ="left")
reset.pack(side="left")

def nextPage1():
    ws.destroy()
    import page3

def nextPage():
    ws.destroy()
    import page1

def prevPage():
    ws.destroy()
    import page2


    
Label(
    ws,
    text="Countdown...",
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
    text=" Next Timer", 
    font=f,
    command=nextPage1,
    background='yellow'
    ).pack(fill=X, expand=TRUE, side=LEFT)

ws.mainloop()