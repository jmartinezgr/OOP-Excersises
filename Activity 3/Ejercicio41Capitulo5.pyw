import tkinter as tk
from tkinter import messagebox

class ListaNumeros():
    def __init__(self, Lista):
        self.Lista = Lista

    def getValorMayor(self):
        return max(self.Lista)


def hacer_operacion():
    seleccionados = numeros_listbox.curselection()
    numeros_seleccionados = [numeros_listbox.get(i) for i in seleccionados]
    lista = ListaNumeros(numeros_seleccionados)
    string = f'Numero mayor: {lista.getValorMayor()} \n'
    messagebox.showinfo("Resultado", string)
    numeros_listbox.delete(0, tk.END)

def agregar():
    if int(numero_entry.get()) >= 0:
        numeros_listbox.insert(tk.END, int(numero_entry.get()))
    else:
        messagebox.showerror("Error", "No se pueden agregar valores negativos")

window = tk.Tk()
window.title("Ejercicio 41 Capitulo 5")
window.geometry("400x400")

numero_label = tk.Label(window, text="Numero:")
numero_label.place(x=50, y=50)
numero_entry = tk.Entry(window)
numero_entry.place(x=150, y=50)

añadir_button = tk.Button(window, text="Añadir", command=agregar)
añadir_button.place(x=190, y=100)

numeros_listbox = tk.Listbox(window, selectmode=tk.MULTIPLE)
numeros_listbox.place(x=150, y=150)

operacion_button = tk.Button(window, text="Realizar Operación", command=hacer_operacion)
operacion_button.place(x=160, y=350)

window.mainloop()
