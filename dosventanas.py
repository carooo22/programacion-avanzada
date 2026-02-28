import tkinter as tk

def ven_principal():
    global ven1
    ven1=tk.Tk()
    ven1.title("ventana principal")
    ven1.geometry("400x300")
    ven1.config(bg="pink")

    eti1=tk.Label(ven1, text="esta es la ventana principal", bg="pink", fg="brown", font=("arial", 16, "bold"))
    eti1.pack()

    boton1=tk.Button(ven1, text="ventana 2", command=ven_principal2)
    boton1.pack(pady=20)

    boton2=tk.Button(ven1, text="ventana 3", command=ven_principal3)
    boton2.pack(pady=20)

    boton3=tk.Button(ven1, text="ventana 4", command=ven_principal4)
    boton3.pack(pady=20)

    boton4=tk.Button(ven1, text="ventana 5", command=ven_principal5)
    boton4.pack(pady=20)

    ven1.mainloop()


def destruir_ventanas(ventana_actual):
    ventana_actual.destroy()
    ven_principal()


def ven_principal2():
    ven1.destroy()
    ven2=tk.Tk()
    ven2.title("ventana 2")
    ven2.geometry("400x300")
    ven2.config(bg="lightblue")

    eti2=tk.Label(ven2, text="esta es la ventana 2", bg="lightblue", fg="black", font=("arial", 16, "bold"))
    eti2.pack()

    boton6=tk.Button(ven2, text="ventana principal", command=lambda:destruir_ventanas(ven2))
    boton6.pack(pady=20)

    ven2.mainloop()


def ven_principal3():
    ven1.destroy()
    ven3=tk.Tk()
    ven3.title("ventana 3")
    ven3.geometry("400x300")
    ven3.config(bg="orange")

    eti2=tk.Label(ven3, text="esta es la ventana 3", bg="orange", fg="black", font=("arial", 16, "bold"))
    eti2.pack()

    boton7=tk.Button(ven3, text="ventana principal", command=lambda:destruir_ventanas(ven3))
    boton7.pack(pady=20)

    ven3.mainloop()

def ven_principal4():
    ven1.destroy()
    ven4=tk.Tk()
    ven4.title("ventana 4")
    ven4.geometry("400x300")
    ven4.config(bg="yellow")

    eti2=tk.Label(ven4, text="esta es la ventana 4", bg="yellow", fg="black", font=("arial", 16, "bold"))
    eti2.pack()

    boton8=tk.Button(ven4, text="ventana principal", command=lambda:destruir_ventanas(ven4))
    boton8.pack(pady=20)

    ven4.mainloop()


def ven_principal5():
    ven1.destroy()
    ven5=tk.Tk()
    ven5.title("ventana 2")
    ven5.geometry("400x300")
    ven5.config(bg="green")

    eti2=tk.Label(ven5, text="esta es la ventana 5", bg="green", fg="black", font=("arial", 16, "bold"))
    eti2.pack()

    boton9=tk.Button(ven5, text="ventana principal", command=lambda:destruir_ventanas(ven5))
    boton9.pack(pady=20)

    ven5.mainloop()

ven_principal()