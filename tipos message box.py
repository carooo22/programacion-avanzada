import tkinter as tk
from tkinter import messagebox

def ventanas():
    if var2.get()==1:
        messagebox.showinfo("ventana de info", "aqui puedes escribir info al usuario")
    elif var2.get()==2:
        messagebox.showwarning("ventana de advertencia", "esta es una advertencia")
    elif var2.get()==3:
        messagebox.showerror("ventana de error", "has cometido un error")
    elif var2.get()==4:
        respuesta=messagebox.askyesno("ventana de opcion", "te gusta la clase")
        if respuesta:
           messagebox.showinfo("ventana de respuesta", "mas te vale")
        else:
           messagebox.showinfo("ventana de respuesta", "por eso vas a reprobar")
    elif var2.get()==5:
        respuesta=messagebox.askokcancel("ventana de opcion", "das tu alma a la clase?")
        if respuesta:
           messagebox.showinfo("ventana de respuesta", "vas a sacar 10")
        else:
           messagebox.showinfo("ventana de respuesta", "vas a reprobar")
    else:
        messagebox.showinfo("ventana de respuesta", "no elegiste respuesta")       


ven3=tk.Tk()
ven3.title("tipos de message box")
ven3.geometry("300x300")
ven3.config(bg="pink")

etiqueta1=tk.Label(ven3, text="uso de las messagebox")
etiqueta1.pack(pady=20)

var2=tk.IntVar()
rad1=tk.Radiobutton(ven3, text="mostrar info", variable=var2, value=1)
rad1.pack()
rad2=tk.Radiobutton(ven3, text="advertencia", variable=var2, value=2)
rad2.pack()
rad3=tk.Radiobutton(ven3, text="error", variable=var2, value=3)
rad3.pack()
rad4=tk.Radiobutton(ven3, text="preguntar si o no", variable=var2, value=4)
rad4.pack()
rad5=tk.Radiobutton(ven3, text="preguntar aceptar o cancelar", variable=var2, value=5)
rad5.pack()

boton1=tk.Button(ven3, text="revisar", command=ventanas)
boton1.pack(pady=30)

ven3.mainloop()