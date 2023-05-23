import tkinter as tk
from tkinter import messagebox
import math

class Ecuacion():
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

    def EncontrarRaiz1(self):
        return (-1*self.b + math.sqrt(self.b**2-4*self.a*self.c))/2*self.a

    def EncontrarRaiz2(self):
        return (-1*self.b - math.sqrt(self.b**2-4*self.a*self.c))/2*self.a

def CalcularEcuacion():
    nuevaEcuacion = Ecuacion(float(a_entry.get()),float(b_entry.get()),float(c_entry.get()))

    string = f'Raiz 1: {nuevaEcuacion.EncontrarRaiz1()} \nRaiz 2: {nuevaEcuacion.EncontrarRaiz2()}'

    messagebox.showinfo("Resultado",string)

window = tk.Tk()
window.title("Ejercicio 22 Capitulo 4")


a_label = tk.Label(window, text="A:")
a_label.grid(row=0, column=0, sticky="e")
a_entry = tk.Entry(window)
a_entry.grid(row=0, column=1,padx=10,pady=10)

b_label = tk.Label(window, text="B:")
b_label.grid(row=2, column=0, sticky="e")
b_entry = tk.Entry(window)
b_entry.grid(row=2, column=1,padx=10,pady=10)

c_label = tk.Label(window, text="C:")
c_label.grid(row=3, column=0, sticky="e")
c_entry = tk.Entry(window)
c_entry.grid(row=3, column=1,padx=10,pady=10)

# Crear botón para calcular
calcular_button = tk.Button(window, text="Calcular",command=CalcularEcuacion)
calcular_button.grid(row=8,columnspan=2,padx=10,pady=10)


window.mainloop()