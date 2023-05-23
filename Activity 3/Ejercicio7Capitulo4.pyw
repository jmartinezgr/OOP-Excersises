import tkinter as tk
from tkinter import messagebox

class Comparacion():
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def comparar(self):
        if self.a > self.b:
            return 1
        else:
            if self.a == self.b:
                return 2
            else:
                return 3

def calcular():
    nuevaComparacion = Comparacion(float(a_entry.get()),float(b_entry.get()))

    resultado = nuevaComparacion.comparar()    
    if resultado == 1:    
        string = f'{float(a_entry.get())} es mayor que {float(b_entry.get())}'
    if resultado == 2:    
        string = f'{float(a_entry.get())} es igual a {float(b_entry.get())}'
    if resultado == 3:    
        string = f'{float(a_entry.get())} es menor que {float(b_entry.get())}'

    messagebox.showinfo("Resultado",string)



window = tk.Tk()
window.title("Ejercicio 7 Capitulo 4")

a_label = tk.Label(window, text="Numero A:")
a_label.grid(row=0, column=0)
a_entry = tk.Entry(window)
a_entry.grid(row=0, column=1,padx=10,pady=10)

b_label = tk.Label(window, text="Numero B:")
b_label.grid(row=1, column=0)
b_entry = tk.Entry(window)
b_entry.grid(row=1, column=1,padx=10,pady=10)

# Crear botón para calcular
calcular_button = tk.Button(window, text="Calcular", command=calcular)
calcular_button.grid(row=8,columnspan=2,padx=10,pady=10)


window.mainloop()