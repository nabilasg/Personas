


class Persona:
    pass

    def __init__(self,dni):
        self.nombre = ""
        self.edad= 0
        self.dni=dni
        self.sexo= 'mujer'
        self.peso= 0
        self.altura= 0


        nombre = str(input("introduzca el nombre: "))
        print(f"el nombre es str{nombre}")

        edad = int(input("introduzca la edad: "))
        print(f"la edad es {edad}")

        dni = str(input("introduzca el dni: "))
        print(f"el dni es  str{dni}")

        sexo = str(input("introduzca el sexo: "))
        print(f"el sexo es str{sexo}")

        peso = int(input("introduzca el peso: "))
        print(f"el peso es {peso}")

        altura = int(input("introduzca la altura: "))
        print(f"la altura es  str{altura}")

    def Personas(self):
        pass
        persona1 = Persona(self)

        persona1.nombre = nombre = str(input("introduzca el nombre: "))
        print(f"el nombre es str{nombre}")


        persona1.edad = edad = int(input("introduzca la edad: "))
        print(f"la edad es {edad}")

        persona1.sexo = sexo = str(input("introduzca el sexo: "))
        print(f"el sexo es str{sexo}")

        persona1.peso = peso = int(input("introduzca el peso: "))
        print(f"el peso es es {peso}")

        persona1.altura = altura = str(input("introduzca la altura: "))
        print(f"la altura es int{altura}")



    def Personas2(self):
        pass
        persona2 = Persona(self)

        persona2.nombre = nombre = str(input("introduzca el nombre: "))
        print(f"el nombre es str{nombre}")

        persona2.edad = edad = int(input("introduzca la edad: "))
        print(f"la edad es {edad}")

        persona2.sexo = sexo = str(input("introduzca el sexo: "))
        print(f"el sexo es str{sexo}")

    def Personas3(self):
        pass
        persona3 = Persona(self)

        persona3.nombre = nombre = str(input("introduzca el nombre: "))
        print(f"el nombre es str{nombre}")

        persona3.edad = edad = int(input("introduzca la edad: "))
        print(f"la edad es {edad}")

        persona3.sexo = sexo = str(input("introduzca el sexo: "))
        print(f"el sexo es str{sexo}")

        persona3.peso = peso = int(input("introduzca el peso: "))
        print(f"el peso es es {peso}")

        persona3.altura = altura = str(input("introduzca la altura: "))
        print(f"la altura es int{altura}")



    def calcularImc(self,sobrepeso,infrapeso,pesoideal):

    @staticmethod
    def sobrepeso():
        print('SOBREPESO')

    @staticmethod
    def infrapeso():
        print("INFRA PESO")


    @staticmethod
    def pesoideal():
        print('PESO IDEAL')



#Lo que quise poner es que cada persona (persona1,persona2,persona3) tuviesen el un metodo que calcula el peso pero me da error

