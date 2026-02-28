import tkinter as tk
from PIL import Image, ImageTk
def boton_clic():
    print("hiciste click")

def actualizar_etiqueta():
    nuevo_texto=entrada.get()
    etiqueta2.config(text=nuevo_texto)    

ven1 = tk.Tk()
ven1.title("mi primera app con tkinter")
ven1.geometry("500x500")

etiqueta= tk.Label(ven1,text="hola clase",
     font=("arial", 14, "bold"), fg="brown", bg="pink", padx=20, pady=10)
etiqueta.pack()

etiqueta2=tk.Label(ven1,text="mi nombre es caro",
     font=("arial", 14, "bold"), fg="brown", bg="pink", padx=20, pady=10)
etiqueta2.pack()

etiqueta3=tk.Label(ven1,text="estudio compu",
     font=("arial", 14, "bold"), fg="brown", bg="pink", padx=20, pady=10)
etiqueta3.pack()

etiqueta4=tk.Label(ven1,text="mi comida fav es la lasaña",
     font=("arial", 14, "bold"), fg="brown", bg="pink", padx=20, pady=10)
etiqueta4.pack()
ven1.mainloop()

root = tk.Tk()
root.title("imagen en tkinter")
imagen = Image.open("elbeso.jpg")
imagen = imagen.resize((400,600))
imagen_tk = ImageTk.PhotoImage(imagen)
label_imagen = tk.Label(root, image=imagen_tk)
label_imagen.pack(pady=20)

boton = tk.Button(root, text="haz click aqui", command=boton_clic,
                  font=("comic sans", 30), fg="brown", bg="pink")
boton.pack(pady=20)
root.mainloop()

ven2 = tk.Tk()
ven2.title("etiqueta dinamica")
entrada = tk.Entry(ven2, width=60)
entrada.pack(pady=10)

boton2 = tk.Button(ven2, text="actualizar", command= actualizar_etiqueta)
boton2.pack()

etiqueta2 = tk.Label(ven2, text="texto inicial", font=("arial",12))
etiqueta2.pack(pady=10)
ven2.mainloop()