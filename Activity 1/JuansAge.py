class JuansAges():    
    def getAge(self):
        #Se pregunta la edad de juan
        return int(input('¿Cuantos años tiene Juan?: '))

    def calculateAges(self):
        #Se ejecuta la funcion que obtiene la edad de Juan
        Juan = self.getAge()
        #Se muestran las edades de los 4
        print(f'La edad de Juan es: {Juan}')
        print(f'La edad de Alberto es: {Juan*2/3}')
        print(f'La edad de Ana es: {Juan*4/3}')
        print(f'La edad de la mama es: {3*Juan}')

#Se ejecuta el codigo
excercise = JuansAges()
excercise.calculateAges()