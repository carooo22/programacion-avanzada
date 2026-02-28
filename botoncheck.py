import tkinter as tk
from tkinter import messagebox

def estatus():
    if var.get()==1:
        messagebox.showinfo("estado", "checkbutton seleccionado")
    else:
        messagebox.showinfo("estado", "checkbutton no esta seleccionado")

ven1=tk.Tk()
ven1.title("uso del checkbutton")
ven1.geometry("400x500")

etiqueta1=tk.Label(ven1, text="aqui voy a poner un checkbutton")
etiqueta1.pack(pady=20)

var=tk.IntVar()
bcheck=tk.Checkbutton(ven1, text="elegir opcion", variable=var)
bcheck.pack(pady=20)
boton1=tk.Button(ven1, text="verificar estatus", command=estatus)
boton1.pack()

ven1.mainloop()