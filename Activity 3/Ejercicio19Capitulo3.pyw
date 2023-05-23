import tkinter as tk
from tkinter import messagebox
import math

class Triangulo():
    def __init__(self,lado):
        self.lado = lado

    def getPerimetro(self):
        return self.lado*3
    
    def getAltura(self):
        return math.sqrt(self.lado**2 - (self.lado/2)**2) 
    
    def getArea(self):
        return math.sqrt(3)*(1/4)*self.lado**2

def calcularMedidas():
    triangulo = Triangulo(float(lado_entry.get()))

    string = f'Perimetro: {triangulo.getPerimetro()} \nAltura: {triangulo.getAltura()} \nArea: {triangulo.getArea()} \n'

    messagebox.showinfo("Resultado",string)


window = tk.Tk()
window.title("Ejercicio 19 Capitulo 3")

lado_label = tk.Label(window, text="Lado:")
lado_label.grid(row=0, column=0)
lado_entry = tk.Entry(window)
lado_entry.grid(row=0, column=1,padx=10,pady=10)

# Crear botón para calcular
calcular_button = tk.Button(window, text="Calcular", command=calcularMedidas)
calcular_button.grid(row=8,columnspan=2,padx=10,pady=10)


window.mainloop()

