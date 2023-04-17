import math

class circle():
    def __init__(self):
        self.r = float(input('Ingresa el radio del circulo: '))

    def setArea(self):
        self.Area = self.r**2 * math.pi
    
    def setPerimeter(self):
        self.P = 2*self.r*math.pi

    def getData(self):
        print(f'El area del circulo es {self.Area}')
        print(f'El perimetro del circulo es {self.P}')

#Inicia el codigo

Excercise = circle()
Excercise.setArea()
Excercise.setPerimeter()
Excercise.getData()