class Calculadora:
    def __init__(self, numero1, numero2):
        self.num1=numero1
        self.num2=numero2
        
    def suma(self):
        total_Sum= self.num1 + self.num2
        print("La suma de los numeros {} y {} es de: {}".format(self.num1,self.num2,total_Sum))
    
    def resta(self):
        total_Res= self.num1 - self.num2
        print("La resta de los numeros {} y {} es de: {}".format(self.num1, self.num2, total_Res))
    
    def multiplicacion(self):
        total_Mul= self.num1 * self.num2
        print("La multiplicación de los numeros {} y {} es de: {}".format(self.num1,self.num2,total_Mul))
                
    def division(self):
        total_Div= self.num1 / self.num2
        print("La division de los 2 numeros es de: {}".format(total_Div))
        
class CalEstandar(Calculadora):
    def __init__(self, numero1, numero2):
        super().__init__(numero1, numero2)
        
        
    def multiplicacion(self):
        return  self.num1 * self.num2
        
    
    def exponente(self):
        total_Exp = self.num1**self.num2
        print("la multiplicacion de {}**{} de la potencia es: {}".format(self.num1,self.num2,total_Exp))

    def valorAbsoluto(self):
        numero= self.num1+self.num2
        if numero < 0:
            numero = numero *- 1
        return numero

    
class calCientifica(Calculadora):

    def __init__(self, numero1, numero2):
        super().__init__(numero1, numero2)
        
    def circunferencia(self):
        PI = 3.1416
        Perimetro = 2 * PI * self.num1
        return Perimetro
    
    def areaCirculo(self):
        PI = 3.1416
        area = PI * (self.num1**2)
        return area
    
    def areaCuadrado(self):
        return self.num1 ** 2
