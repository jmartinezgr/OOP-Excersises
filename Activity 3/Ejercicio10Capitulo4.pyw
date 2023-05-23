import tkinter as tk
from tkinter import messagebox

class Estudiante():
    def __init__(self,numero,nombre):
        self.numeroIns = numero
        self.nombre = nombre

    def getNumero(self):
        return self.numeroIns
    
    def getNombre(self):
        return self.nombre
    
    def setPatrimonio(self,valor):
        self.patrimonio = valor
    
    def setEstrato(self,estrato):
        self.estrato = estrato

    def getMatricula(self):
        if self.patrimonio > 2000000 and self.estrato > 3:
            return 50000+(self.patrimonio*0.03) 

def calcular_matricula():
    
    estudiante = Estudiante(numero=numero_inscripcion_entry.get(),nombre=nombre_entry.get())
    estudiante.setEstrato(estrato=int(estrato_entry.get()))
    estudiante.setPatrimonio(valor=float(patrimonio_entry.get()))

    valor = estudiante.getMatricula()

    string = f'Numero Inscripcion: {estudiante.getNumero()} \nNombres: {estudiante.getNombre()} \nMatricula: {estudiante.getMatricula()}'

    messagebox.showinfo("Resultado",string)


window = tk.Tk()
window.title("Ejercicio 10 Capitulo 4")

window.geometry("400x250")

numero_inscripcion_label = tk.Label(window, text="Numero Inscripcion:")
numero_inscripcion_label.grid(row=0, column=0, sticky="e")
numero_inscripcion_entry = tk.Entry(window)
numero_inscripcion_entry.grid(row=0, column=1,padx=10,pady=10,sticky="e")

nombre_label = tk.Label(window, text="Nombres:")
nombre_label.grid(row=1, column=0, sticky="e")
nombre_entry = tk.Entry(window)
nombre_entry.grid(row=1, column=1,padx=10,pady=10)

patrimonio_label = tk.Label(window, text="Patrimonio:")
patrimonio_label.grid(row=2, column=0,sticky="e")
patrimonio_entry = tk.Entry(window)
patrimonio_entry.grid(row=2, column=1,padx=10,pady=10,sticky="e")

estrato_label = tk.Label(window, text="Estrato:")
estrato_label.grid(row=3, column=0,sticky="e")
estrato_entry = tk.Entry(window)
estrato_entry.grid(row=3, column=1,padx=10,pady=10,sticky="e")

# Crear botón para calcular el salario
calcular_button = tk.Button(window, text="Calcular", command=calcular_matricula)
calcular_button.grid(row=8,columnspan=2,padx=10,pady=10)


window.mainloop()

