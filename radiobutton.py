import tkinter as tk
from tkinter import messagebox

def opcion():
    if var.get()==1:
        messagebox.showinfo("hola", "te gustan los tacos")
    elif var.get()==2:
        messagebox.showinfo("hola", "te gusta la milanesa")
    elif var.get()==3:    
        messagebox.showinfo("hola", "te gusta la pizza")
    elif var.get()==4:
        messagebox.showinfo("hola", "te gustan las hamburguesas")    

ven2=tk.Tk()
ven2.title("radiobutton")
ven2.geometry("300x300")

etiqueta1=tk.Label(ven2, text="cual es tu comida favorita?")
etiqueta1.pack(pady=20)

var=tk.IntVar()
rad1=tk.Radiobutton(ven2, text="tacos", variable=var, value=1)
rad1.pack()
rad3=tk.Radiobutton(ven2, text="milanesa", variable=var, value=2)
rad3.pack()
rad4=tk.Radiobutton(ven2, text="pizza", variable=var, value=3)
rad4.pack()
rad5=tk.Radiobutton(ven2, text="hamburguesa", variable=var, value=4)
rad5.pack()

boton1=tk.Button(ven2, text="verificar", command=opcion)
boton1.pack(pady=30)

ven2.mainloop()