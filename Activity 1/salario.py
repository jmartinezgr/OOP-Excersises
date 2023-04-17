class Salario():
    def __init__(self):
        self.salarioHora = 5000
        self.horaSemana = 48
        self.retencion = 0.125
    
    def salarioBru(self):
        self.salarioBruto = self.salarioHora*self.horaSemana

    def retencionFuente(self):
        self.retencionTotal = self.salarioBruto*self.retencion
    
    def salarioNe(self):
        self.salarioNeto = self.salarioBruto-self.retencionTotal

    def getData(self):
        print(f'El salario bruto es: {self.salarioBruto}')
        print(f'La retención en la fuente es: {self.retencionTotal}')
        print(f'El salario neto es: {self.salarioNeto}')

#Inicia el codigo

Excercise = Salario()
Excercise.salarioBru()
Excercise.retencionFuente()
Excercise.salarioNe()
Excercise.getData()
