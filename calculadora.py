class Calculadora:
    def __init__(self, numero1, numero2):
        self.num1 = numero1
        self.num2 = numero2
    
    def suma(self):
        return self.num1 + self.num2
    
    
    def resta(self):
        return self.num1 - self.num2
    
    
    def mutiplicacion(self):
        multi = self.num1 * self.num2
        print("{}*{}={}".format(self.num1,self.num2,multi))
    
    
    def división(self):
        return self.num1 / self.num2
        
         


class CalEstandar(Calculadora):
    def __ini__(self, numero1, numero2):
            super()._init_(numero1,numero2)


    def mutiplicacion(self): # aplicar polimorfismo
        return self.num1 * self.num2   
    
    
    def exponente(self):
        pass
    
    
    def valorAbsoluto(self,numero):
        if numero <0:
            numero = numero*-1
        return numero


class CalCientifica(Calculadora):
    PI = 3.1416 
    def __init__(self, numero1, numero2):
            super()._init_(numero1,numero2)
    
    
    def  circunferencia(radio):
        print
