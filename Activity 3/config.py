from tkinter import *
import os.path

class Program:
    def __init__(self,name,rezisable=False):
        self.title = f'Ejercicio {name[0]} - Capitulo {name[1]}'
        self.icon = './images/Logotipo_de_la_Universidad_Nacional_de_Colombia.ico'
        self.alter_icon = './Activity 3/images/Logotipo_de_la_Universidad_Nacional_de_Colombia.ico'
        self.size = "770x470"
        self.resizable = rezisable
        self.background = '#CCC'
        self.bd = 50

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

        self.executable.config(
            bd=self.bd,
            bg=self.background
        )

    def start(self):
        self.executable.mainloop()


