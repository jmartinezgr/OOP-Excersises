import tkinter as tk
from tkinter import messagebox

class Trabajador():
    def __init__(self,nombre,horas,valor):
        self.nombre = nombre
        self.horas = horas
        self.valor = valor

    def getNombre(self):
        return self.nombre
    
    def getHoras(self):
        return self.horas
    
    def getValor(self):
        return self.valor
    
    def calcSalario(self):

        return self.horas*self.valor

def verificar():
    trabajador = Trabajador(nombre=nombre_entry.get(),horas=int(horas_entry.get()),valor=int(valor_entry.get()))

    if trabajador.calcSalario() > 450000:
        string = f'Nombre: {trabajador.getNombre()} \nSalario Mensual: {trabajador.calcSalario()}'
    else:
        string = f'Nombre: {trabajador.getNombre()}'

    messagebox.showinfo("Resultado",string)

window = tk.Tk()
window.title("Ejercicio 22 Capitulo 4")
window.geometry("400x200")

nombre_label = tk.Label(window, text="Nombres:")
nombre_label.grid(row=0, column=0, sticky="e")
nombre_entry = tk.Entry(window)
nombre_entry.grid(row=0, column=1,padx=10,pady=10)

horas_label = tk.Label(window, text="                 Horas Trabajadas al Mes:")
horas_label.grid(row=2, column=0, sticky="e")
horas_entry = tk.Entry(window)
horas_entry.grid(row=2, column=1,padx=10,pady=10)

valor_label = tk.Label(window, text="Valor Hora Trabajada:")
valor_label.grid(row=3, column=0, sticky="e")
valor_entry = tk.Entry(window)
valor_entry.grid(row=3, column=1,padx=10,pady=10)

# Crear botón para calcular
calcular_button = tk.Button(window, text="Calcular",command=verificar)
calcular_button.grid(row=8,columnspan=2,padx=10,pady=10)


window.mainloop()