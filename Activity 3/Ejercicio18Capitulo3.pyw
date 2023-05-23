import tkinter as tk
from tkinter import messagebox

class Empleado():
    def __init__(self,nombre,codigoEmpleado):
        self.nombre = nombre
        self.codigoEmpleado = codigoEmpleado
    
    #Funciones set
    def setHorasTrabajadas(self,horas):
        self.HorasTrabajadas = horas
    
    def setValorHora(self,valor):
        self.ValorHora = valor

    def setPorcentajeRetencion(self,porcentaje):
        self.PorcentajeRetencion = porcentaje

    #Metodos get
    def getNombres(self):
        return self.nombre
    
    def getCodigo(self):
        return self.codigoEmpleado
    
    def getSalarioBruto(self):
        return self.ValorHora*self.HorasTrabajadas
    
    def getSalarioNeto(self):
        return self.ValorHora*self.HorasTrabajadas*(1-(self.PorcentajeRetencion/100))

def calcular_salario():
    nuevo = Empleado(nombre=nombre_entry.get(),codigoEmpleado=codigo_entry.get())

    nuevo.setHorasTrabajadas(horas=float(horas_entry.get()))
    nuevo.setValorHora(valor=float(valor_entry.get()))

    nuevo.setPorcentajeRetencion(porcentaje=float(retencion_entry.get()))

    string = f'Nombres: {nuevo.getNombres()} \n Codigo: {nuevo.getCodigo()} \n Salario  neto: {nuevo.getSalarioNeto()} \n Salario Bruto {nuevo.getSalarioBruto()}'

    messagebox.showinfo("Resultado",string)


#Ejecutando las configuraciones generales de la ventana ejecutable
window = tk.Tk()
window.title("Ejercicio 18 Capitulo 3")

window.geometry("400x250")

nombre = tk.StringVar()
apellidos = tk.StringVar()
horasTrabadas = tk.StringVar()
valorHora = tk.StringVar()
retencion = tk.StringVar()

nombre_label = tk.Label(window, text="Nombres:")
nombre_label.grid(row=0, column=0, sticky="e")
nombre_entry = tk.Entry(window)
nombre_entry.grid(row=0, column=1,padx=10,pady=10)


codigo_label = tk.Label(window, text="Codigo:")
codigo_label.grid(row=1, column=0, sticky="e")
codigo_entry = tk.Entry(window)
codigo_entry.grid(row=1, column=1,padx=10,pady=10)

horas_label = tk.Label(window, text="Horas Trabajadas al Mes:")
horas_label.grid(row=2, column=0, sticky="e")
horas_entry = tk.Entry(window)
horas_entry.grid(row=2, column=1,padx=10,pady=10)

valor_label = tk.Label(window, text="Valor Hora Trabajada:")
valor_label.grid(row=3, column=0, sticky="e")
valor_entry = tk.Entry(window)
valor_entry.grid(row=3, column=1,padx=10,pady=10)

retencion_label = tk.Label(window, text="Porcentaje Retención en la Fuente:")
retencion_label.grid(row=4, column=0, sticky="e")
retencion_entry = tk.Entry(window)
retencion_entry.grid(row=4, column=1,padx=10,pady=10)

# Crear botón para calcular el salario
calcular_button = tk.Button(window, text="Calcular", command=calcular_salario)
calcular_button.grid(row=8,columnspan=2,padx=10,pady=10)


window.mainloop()

