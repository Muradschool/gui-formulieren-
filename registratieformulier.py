import tkinter as tk
from tkinter import N, ttk
import tkinter.messagebox

gui = tk.Tk()
gui.geometry('500x500')
gui.title('Registratie Formulier')
gui.config(bg='white')


Title = tk.Label(
    gui,
    text= ('Registratie Formulier'),
    font=('arial',20, 'bold'),
    bg="white",
    fg="black"
)
Title.place(x=100, y=2)


Naam = ttk.Entry(
    gui,
)
Naam.place(x= 105, y=55)

NaamWoord = tk.Label(
    gui,
    text="Naam:",
    font=('arial', 10, 'bold'),
    bg="white"
)
NaamWoord.place(x=55, y=55)


AchterNaam = ttk.Entry(
    gui,
)
AchterNaam.place(x=105, y=90)

AchterNaamWoord = tk.Label(
    gui,
    text="Achternaam:",
    font=('arial', 10, 'bold'),
    bg="white"
)
AchterNaamWoord.place(x=15, y=90)


Email = ttk.Entry(
    gui,
)
Email.place(x=105, y=125)

EmailWoord = tk.Label(
    gui,
    text="E-mail:",
    font=('arial', 10, 'bold'),
    bg='white'
)
EmailWoord.place(x=45, y=125)


Gender = ttk.Combobox(gui, values=("Man","Vrouw", "Non-Binair"))
Gender.place(x=105, y=180)

GenderWoord = tk.Label(
    gui,
    text="Gender:",
    font=('arial', 10, 'bold'),
    bg='white'
)
GenderWoord.place(x=45, y=180)

Guest = ttk.Combobox(gui, values=("Ja","Nee"))
Guest.place(x=105, y=215)

GuestWoord = tk.Label(
    gui,
    text="Guest:",
    font=('arial', 10, 'bold'),
    bg='white'
)
GuestWoord.place(x=55, y=215)


Opmerking = ttk.Entry(
    gui,
)
Opmerking.place(x=105, y=275)

OpmerkingWoord = tk.Label(
    gui,
    text="Opmerking:",
    font=('arial', 10, 'bold'),
    bg='white'
)
OpmerkingWoord.place(x=20, y=275)


Save = tk.Button(
    gui,
    text="Save",
    font=('arial', 20, 'bold'),
    bg='white',
    command=lambda: [AllesOpslaan()]
)
Save.place(x=300, y=350)

def AllesOpslaan():
    tekst = Naam.get() +'\n'+ AchterNaam.get() +'\n'+ Email.get() + '\n' + Gender.get() + '\n' + Opmerking.get()
    tkinter.messagebox.showinfo('hello', tekst)

gui.mainloop()