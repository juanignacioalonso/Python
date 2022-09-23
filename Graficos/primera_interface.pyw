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

raiz.resizable(0,0)#Modificacion de el tamaño de la ventana

#raiz.iconbitmap("favicon.ico") para cambiar el icono de la ventana

raiz.geometry("650x350")

raiz.config(bg="black")

raiz.mainloop()  #Este metodo debe ir siempre al final
 