import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import askyesno
import sys
import os
import random

# alle code komt hier tussen
gui = tk.Tk()
gui.title('FPStrainer')
gui.geometry("{0}x{1}+0+0".format(gui.winfo_screenwidth(), gui.winfo_screenheight()))
gui.config(bg="grey")
label = tk.Label(gui)
textbox = ttk.Entry(gui)

temptimer = 0
timer = 20
points = 0
randomPosition = random.randint(0, 500)
buttons=['Press: w', 'Press: a', 'Press: s', 'Press: d', 'Press: spacebar', 'One click', 'Double click', 'Triple click']
buttonBinds=['<w>', '<a>', '<s>', '<d>', '<space>', '<Button>', '<Double-Button>', '<Triple-Button>']
var1 = random.randint(0,7)


def message():
    global points
    answer = askyesno(title='Melding',
                    message='Je hebt '+ str(points) +' punten gehaald! Wil je nog een keer?')
    if answer:
        restart()
    else:
        gui.destroy()


def countdown():
    global timer
    if timer > -1:
        timer = timer
        timer_Label.config(text='Time: '+ str(timer),font=('arial',25))
        timer = timer - 1
        gui.after(1000, countdown)
    if timer == 0:
        message()

timer_Label=tk.Label(
gui, 
text='Time: '+ str(timer),
font=('arial',25),
fg='black',
bg='gray')
timer_Label.place(anchor="nw")


points_Label=tk.Label(
gui, 
text='Points: '+ str(points),
font=('arial',25),
fg='black',
bg='gray')
points_Label.place(x='1380')

def addPoints(e):
    global points,var1
    gui.unbind(buttonBinds[var1],funcid=None)
    var1 = random.randint(0,7)
    points += 1
    points_Label.config(text="Points: "+str(points))
    gui.bind(buttonBinds[var1],addPoints)
    clickbutton.configure(
        text=(buttons[var1]))       
    clickbutton.place(x=random.randint(0,500), y=random.randint(0,500))


def starter():    
    start_button = tk.Button(
    gui, 
    text='Press to start', 
    font=('arial',35,'bold'),
    fg='white',bg='black',
    command = lambda:[start_button.destroy(), countdown(), randombutton(), bindfunction()] )
    start_button.place(relx=.5, rely=.5, anchor="center")


def bindfunction():
    gui.bind(buttonBinds[var1],addPoints)
def unbind():
    gui.unbind(buttonBinds[var1],addPoints)

def moving():
    clickbutton.place(x=randomPosition, y=randomPosition)


clickbutton = tk.Label(
    gui,
    text=(buttons[var1]),
    font=('arial',20),
    fg='white',
    bg='black',
    padx= 10,
    pady= 10
    )

def randombutton():
    clickbutton.configure(
        text=(buttons[var1])
        )
    clickbutton.place(x=random.randint(0,500), y=random.randint(0,500))


entrytime = tk.Label(
    gui,
    text='Op hoeveel wil je de timer zetten? (standaard = 20)''↓',
    font=('arial',15),
    padx=20,
    pady=20
) 

temptimer = tk.Entry(gui)
entrytime.pack(pady=50)
temptimer.pack(pady=50)

confirm = tk.Button(
    gui,
    text='Confirm',
    font=('arial',15,'bold'),
    fg='black',
    bg='white',
    command= lambda:[starter(), confirm.destroy(), entrytime.destroy(), temptimer.destroy(), timecheck() ]
)
confirm.pack()

def timercheck():
    global temptimer, timer
    timer = (temptimer.get())
    if timer == '':
        timer = 20
    elif timer > '0':
        timer == int(temptimer.get())


def restart():
    python = sys.executable
    os.execl(python, python, * sys.argv)

# alle code komt hier tussen
gui.mainloop()