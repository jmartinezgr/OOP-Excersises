from tkinter import *
import os.path

class Program:
    def __init__(self,name,rezisable=False):
        self.title = f'Ejercicio {name[0]} - Capitulo {name[1]}'
        self.icono = './imagenes/descarga.ico'
        self.alter_icon = './Activity 3/imagenes/descarga.ico'
        self.size=  "770X470"
        self.rezisable = rezisable


