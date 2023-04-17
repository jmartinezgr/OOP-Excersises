class elevate():
    def setNum(self):
        self.num = int(input('Ingrese un numero: '))

    def getSquare(self):
        print(f'El cuadrado de {self.num} es {self.num**2}')

    def getCube(self):
        print(f'El cubo de {self.num} es {self.num**3}')

#Inicia el codigo
Excercise = elevate()
Excercise.setNum()
Excercise.getSquare()
Excercise.getCube()