import tkinter as tk

gui = tk.Tk()
gui.geometry("640x590")
gui.title("Dambord")

frame = tk.Frame(gui)
m = True

for b in range(10):
    m = not m
    for c in range(10):
        if m == False:
            color = "black"
        else: 
            color = "white"
        m = not m
        tile = tk.Label(frame, bg = color, padx = 30, pady = 20)
        tile.grid(row = b, column = c)
frame.pack()

gui.mainloop()