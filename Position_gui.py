from tkinter import *
from tkinter import messagebox

f = ('Times', 14)

def compute_area():
   position = tLength.get()

   if position == 'CLERK':
       rate = 250
       hours = float(tWidth.get())
       pay = rate * hours
       tax = pay *.12
       pay = pay + tax
       messagebox.showinfo('confirmation', 'Total = ' + str(pay))

   elif position == 'SUPERVISOR':
        rate = 450
        hours = float(tWidth.get())
        pay = rate * hours
        tax = pay *.12
        pay = pay + tax
        messagebox.showinfo('confirmation', 'Total = ' + str(pay))

   elif position == 'MANAGER':
        rate = 650
        hours = float(tWidth.get())
        pay = rate * hours
        tax = pay * .12
        pay = pay + tax
        messagebox.showinfo('confirmation', 'Total = ' + str(pay))

ws = Tk()
ws.title('Area Calculator')
ws.geometry('400x300')
ws.config(bg='#0B5A81')

frame = Frame(
    ws,
    bd=2,
    bg='#CCCCCC',
    relief=SOLID,
    padx=10,
    pady=10
)

Label(
    frame,
    text="LIST OF POSITON [CLERK, MANAGER, SUPERVISOR]",
    bg='#CCCCCC',
    font=f).grid(row=0, column=0, sticky=W, pady=10)

Label(
    frame,
    text="HOUR",
    bg='#CCCCCC',
    font=f
).grid(row=1, column=0, pady=10)

tLength = Entry(
    frame,
    font=f
)
tWidth = Entry(
    frame,
    font=f
)
bCompute = Button(
    frame,
    width=15,
    text='Compute',
    font=f,
    relief=SOLID,
    cursor='hand2',
    command=compute_area
)

tLength.grid(row=0, column=1, pady=10, padx=20)
tWidth.grid(row=1, column=1, pady=10, padx=20)
bCompute.grid(row=2, column=1, pady=10, padx=20)
frame.place(x=50, y=50)

ws.mainloop