from tkinter import *
import os.path

class Program:
    def __init__(self,name,rezisable=False):
        self.title = f'Ejercicio {name[0]} - Capitulo {name[1]}'
        self.icon = './imagenes/descarga.ico'
        self.alter_icon = './Activity 3/imagenes/descarga.ico'
        self.size=  "770X470"
        self.resizable = rezisable

    def load(self): 
        #Crear la ventana Raiz
        self.executable = Tk()
        
        #Titulo de la ventana
        self.executable.title(self.title)

        #Comprobar  si existe un archivo
        self.icon_address = os.path.abspath(self.icon)
        if not os.path.isfile(self.icon_address):
            self.icon_address = os.path.abspath(self.alter_icon)

        #Icono de la ventana
        self.executable.iconbitmap(self.icon_address)

        #Cambio en el tamaño de la ventana
        self.executable.geometry(self.size)

        #Bloquear el tamaño de la ventana
        if self.resizable:
            self.executable.resizable(1,1)
        else:
            self.executable.resizable(0,0)


Programa = Program(('18','3'),True)
Programa.load()
Programa.executable.mainloop()