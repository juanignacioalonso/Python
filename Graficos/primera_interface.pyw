"""
Interfaz Gráficas tambien denominadas GUI, son intermediarios entre el programa y el usuario. Formadas por un conjunto de graficos
como ventanas, botones, menús, casillas de verificación etc.

Librerias de python para trabajar con GUI
Tkinter, WxPython,PyQT, PyGTK

Tkinter es un puente entre Python y la libreria TCL/TK

"""
from tkinter import *

raiz = Tk()

raiz.title("Ventana de pruebas")

#raiz.resizable(1,0)#Modificacion de el tamaño de la ventana

#raiz.iconbitmap("favicon.ico") para cambiar el icono de la ventana

#raiz.geometry("650x350") La raiz se adapta al tamaño de el frame, pero la podemos redimencionar

raiz.config(bg="black")

miFrame=Frame()#Lo que agregamos en la raíz

#miFrame.pack(side="right",anchor="s")
#miFrame.pack(fill="y",expand="t")
#miFrame.pack(fill="x",expand="t")
#miFrame.pack(fill="both",expand="t")

miFrame.pack()

miFrame.config(relief="sunken")

miFrame.config(bg="red")

miFrame.config(width="650",height="350")#El frame tiene un tamaño fijo

miFrame.config(bd=35)
miFrame.config(cursor="hand2")

raiz.mainloop()  #Este metodo debe ir siempre al final
 