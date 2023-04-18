import config
from tkinter import *

#Ejecutando las configuraciones generales de la ventana ejecutable
program = config.Program((18,3))
program.load()

nombre = StringVar()
apellidos = StringVar()
horasTrabadas = StringVar()
valorHora = StringVar()
retencion = StringVar()



program.start()


