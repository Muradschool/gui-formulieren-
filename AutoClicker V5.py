import tkinter as tk

clicks = 0
checks = " "
# alle tkinter code komt hier tussen
gui = tk.Tk()

gui.title("Clicker V4")
gui.geometry("500x500")
gui.config(bg= "gray")
clicks = 0 


def Colors(aantal)->str:
    kleur = "gray"
    if aantal < 0:
        kleur = "red"
    elif aantal > 0:
        kleur = "green" 
    return kleur


def up():
    global clicks, checks
    counter(+1)
    checks ="up"


def down():
    global clicks, checks
    counter(-1)
    checks ="down"


def counter(num):
    global clicks, checks
    clicks += num
    gui.configure(bg=Colors(clicks))
    PointLabel.config(text=clicks)
    print(clicks)


def Enter(event):
    gui.configure(bg="yellow")


def Leave(event):
    global clicks
    gui.configure(bg=Colors(clicks))

def doubleclicks(event):
    global checks, clicks
    if checks == "up":
        clicks *= 3
    elif checks == "down":
        clicks /= 3 
    PointLabel.config(text= clicks)


#box 1
ButtonUp = tk.Button(
text="Up",
font=("arial",25,"bold"),
bg="white",
fg="black",
command=up
)
ButtonUp.pack()


#box 2
ButtonDown = tk.Button(
text="Down",
font=("arial",25,"bold"),
bg="white",
fg="black",
command=down
)
ButtonDown.place(relx=.5, rely=.65, anchor="s")


#box 3
PointLabel = tk.Label(
text=clicks,
font=("arial",25,"bold"),
bg="white",
fg="black",
)
PointLabel.place(relx=.5, rely=.3, anchor="center")

def clicks_config():
    PointLabel.config(text=clicks)
    gui.after(200, autoclick)


var1= tk.IntVar()

def autoclick():
    global clicks,checks
    if int(var1.get()) == 1:
        if checks == 'up':
            clicks += 1
            clicks_config()
        elif checks == 'down':
            clicks -= 1
            clicks_config()


autoclick_button = tk.Checkbutton(
    gui,
    text='Autoclicker',
    variable= var1,
    onvalue=1,
    offvalue=0,
    command= autoclick
)
autoclick_button.place(relx=.5, rely=.37, anchor="center")

PointLabel.bind("<Enter>", Enter)
PointLabel.bind("<Leave>", Leave)
PointLabel.bind("<Double-Button>", doubleclicks)
gui.bind("<Up>", up)
gui.bind("<Down>", down)
gui.bind("<space>", doubleclicks)
# alle tkinter code komt hier tussen
gui.mainloop()