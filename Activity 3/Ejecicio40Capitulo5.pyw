import tkinter as tk
import math
from tkinter import messagebox

class Numero():
    def __init__(self,valor):
        self.valor = valor

    def getValor(self):
        return self.valor

    def getsqrt(self):
        return math.sqrt(self.valor)
    
    def getcuadrado(self):
        return self.valor**2
    
    def getcubo(self):
        return self.valor**3


def hacer_operacion():
    seleccionado = numeros_listbox.curselection()
    if seleccionado:
        numero_seleccionado = numeros_listbox.get(seleccionado[0])
        if numero_seleccionado >=0:
            numero = Numero(numero_seleccionado)
            string = f'Numero: {numero.getValor()} \nRaiz: {numero.getsqrt()} \nCuadrado: {numero.getcuadrado()} \nCubo: {numero.getcubo()}'
            messagebox.showinfo("Resultado",string)
        else:
            messagebox.showerror("Error","Debe ser un numero positivo")

def agregar():
    numeros_listbox.insert(tk.END, int(numero_entry.get()))



window = tk.Tk()
window.title("Ejercicio 40 Capitulo 5")

window.geometry("400x400")

numero_label = tk.Label(window, text="Numero:")
numero_label.place(x=50,y=50)
numero_entry = tk.Entry(window)
numero_entry.place(x=150,y=50)

añadir_button = tk.Button(window, text="Añadir", command=agregar)
añadir_button.place(x=190,y=100)


numeros_listbox = tk.Listbox(window, selectmode=tk.SINGLE)
numeros_listbox.place(x=150,y=150)


operacion_button = tk.Button(window, text="Realizar Operación", command=hacer_operacion)
operacion_button.place(x=160,y=350)


window.mainloop()