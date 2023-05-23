import math
import tkinter as tk
from tkinter import messagebox
from tkinter.simpledialog import askfloat

class Circulo:
    def __init__(self,radio):
        self.radio = radio
    
    def calcular_area(self):
        return math.pi*(self.radio**2)

    def calcular_perimetro(self):
        return 2*math.pi*self.radio
    
class Rectangulo:
    def __init__(self,base,altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura
    
    def calcular_perimetro(self):
        return (2*self.base) + (2*self.altura)
    
class Cuadrado:
    def __init__(self,lado):
        self.lado = lado
    
    def calcular_area(self):
        return self.lado * self.lado
    
    def calcular_perimetro(self):
        return self.lado * 4 

class TrianguloRectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return 0.5 * self.base * self.altura

    def calcular_perimetro(self):
        hipotenusa = math.sqrt((self.base**2)+(self.altura**2))
        return self.base + self.altura + hipotenusa

    def calcular_hipotenusa(self):
        return math.sqrt(self.base ** 2 + self.altura ** 2)

    def determinar_tipo(self):
        hipotenusa = math.sqrt((self.base**2)+(self.altura**2))
        if self.base == self.altura and hipotenusa==self.base:
            return "Equilátero"
        elif self.base != self.altura and hipotenusa!= self.base:
            return "Escaleno"
        else:
            return "Isósceles"   


class Rombo:
    def __init__(self, diagonal_mayor, diagonal_menor):
        self.diagonal_mayor = diagonal_mayor
        self.diagonal_menor = diagonal_menor

    def calcular_area(self):
        return (self.diagonal_mayor * self.diagonal_menor) / 2

    def calcular_perimetro(self):
        return self.diagonal_mayor * 2 + self.diagonal_menor * 2
    
class Trapecio:
    def __init__(self, base_mayor, base_menor, altura, lado1, lado2):
        self.base_mayor = base_mayor
        self.base_menor = base_menor
        self.altura = altura
        self.lado1 = lado1
        self.lado2 = lado2

    def calcular_area(self):
        return (self.base_mayor + self.base_menor) * self.altura / 2

    def calcular_perimetro(self):
        return self.base_mayor + self.base_menor + self.lado1 + self.lado2

def crear():
    figura_seleccionada = menu_var.get()

    if  figura_seleccionada == 'Círculo':
        radio = askfloat("Ingresar Dato", "Ingrese el radio del circulo:")
        if radio is not None:
            figura = Circulo(radio=radio)
    
    if  figura_seleccionada == 'Rectángulo':
        base = askfloat("Ingresar Dato", "Ingrese la base del rectangulo:")
        altura = askfloat("Ingresar Dato", "Ingrese la altura del rectangulo:")
        if base is not None and altura is not None :
            figura = Rectangulo(altura=altura,base=base)

    if figura_seleccionada == 'Cuadrado':
        lado = askfloat("Ingresar Dato", "Ingrese el lado del cuadrado:")
        if lado is not None:
            figura = Cuadrado(lado=lado)
        
    if figura_seleccionada == 'Triángulo Rectángulo':
        base = askfloat("Ingresar Dato", "Ingrese la base del Triangulo:")
        altura = askfloat("Ingresar Dato", "Ingrese la altura del Triangulo:")
        if base is not None and altura is not None :
            figura = TrianguloRectangulo(altura=altura,base=base)
    
    if figura_seleccionada == 'Rombo':
        diagonalM = askfloat("Ingresar Dato", "Ingrese la diagonal mayor del rombo:")
        diagonalm = askfloat("Ingresar Dato", "Ingrese la diagonal menor del rombo:")
        if diagonalM is not None  and diagonalm is not None:
            figura = Rombo(diagonal_mayor=diagonalM,diagonal_menor=diagonalm)

    if figura_seleccionada == 'Trapecio':
        baseM = askfloat("Ingresar Dato", "Ingrese la diagonal mayor del rombo:")
        basem = askfloat("Ingresar Dato", "Ingrese la diagonal mayor del rombo:")
        altura = askfloat("Ingresar Dato", "Ingrese la diagonal mayor del rombo:")
        lado1 = askfloat("Ingresar Dato", "Ingrese la diagonal mayor del rombo:")
        lado2 = askfloat("Ingresar Dato", "Ingrese la diagonal mayor del rombo:")
        figura = Trapecio(base_mayor=baseM,base_menor=basem,altura=altura,lado1=lado1,lado2=lado2)

    string = f'Area: {float(figura.calcular_area())} \nPerimetro: {float(figura.calcular_perimetro())}'

    messagebox.showinfo("Area y Perimetro",string)

window = tk.Tk()
window.title("Figuras Geometricas")
window.geometry("200x150")

menu_var = tk.StringVar(window)
menu_var.set("Círculo")  # Opción por defecto

menu = tk.OptionMenu(window, menu_var, "Círculo", "Cuadrado", "Rectángulo", "Triángulo Rectángulo", "Rombo", "Trapecio")
menu.pack(pady=20)

# Botón
calcular_button = tk.Button(window, text="Crear", command=crear)
calcular_button.pack()


window.mainloop()
