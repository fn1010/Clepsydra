import tkinter
from tkinter import *
import PIL
from PIL import ImageTk, Image
 
# importing strftime function to
# retrieve system's time
from time import strftime
ws = Tk()
ws.geometry('1400x600')
ws.title('Clepsydra')
ws['bg']='purple'

f = ("Times bold", 22)


def nextPage():
    ws.destroy()
    import page2
    
def nextPage1():
    ws.destroy()
    import page4
    

def prevPage():
    ws.destroy()
    import page3
    
Label(
    ws,
    text="Welcome to Clepsydra",
    background='purple',
    foreground='white',
    font=f
).pack(expand=TRUE)

frame = Frame(ws,)
frame.pack()

# Create an object of tkinter ImageTk

img = ImageTk.PhotoImage(Image.open("clock.jpg"))

# Create a Label Widget to display the text or Image
label = Label(frame, image = img)
label.pack()

def time():
    string = strftime('%H:%M:%S %p')
    lbl.config(text=string)
    lbl.after(1000, time)
 
 
# Styling the label widget so that clock
# will look more attractive
lbl = Label(ws, font=('calibri', 40, 'bold'),
            background='purple',
            foreground='white')
 
# Placing clock at the centre
# of the tkinter window
lbl.pack(anchor='center',padx=20,pady=20)
time()

Button(
    ws, 
    text="Alarm", 
    font=f,
    command=nextPage,
    background='yellow'
    ).pack(fill=X, expand=TRUE, side=LEFT)

Button(
    ws, 
    text="Stopwatch", 
    font=f,
    command=nextPage1,
    background='yellow'
    ).pack(fill=X, expand=TRUE, side=LEFT)


Button(
    ws, 
    text="Timer", 
    font=f,
    command=prevPage,
    background='yellow'
    ).pack(fill=X, expand=TRUE, side=LEFT)

ws.mainloop()
