import os
from calculadora import CalEstandar,calCientifica,Calculadora

class Menu:
    def __init__(self,titulo,opciones=[]):
        self.titulo=titulo
        self.opciones=opciones

    def menu(self):
        print(self.titulo)
        for opcion in self.opciones:
            print(opcion)
        opc= input("Elija opcion[1...{}]:".format(len(self.opciones)))
        print("")
        return  opc

opc=""
while opc!="5":
    
    os.system("cls")
    men = Menu("Menu Principal",["1). Calculadora","2). Operación Numeros","3). Tratamiento de Listas", "4). Operaciones de  Cadenas","5). Salir"])
    opc = men.menu()

    if opc == "1":
        os.system("cls")
        opc1=""
        while opc1 !="10":
            os.system("cls")
            print("Calculadora")
            men1=Menu("Menu secundario",["1)Suma ","2)Resta","3)Multiplicacion","4)Division","5)Exponente","6)Valor Absoluto","7)Circunferencia","8)Area Circulo","9)Area Cuadrado","10)Salir"])
            opc1=men1.menu()
            os.system("cls")
            if opc1 == "1":
                
                print("Calculadora suma")
                print(" ")
                n1=int(input("ingrese un numero: "))
                n2=int(input("ingrese un numero: "))
                cal = CalEstandar(n1,n2)
                cal.suma()
                input("Presione una tecla para continuar....")
                    


            elif opc1 == "2":
                print("Calculadora Resta")
                print(" ")  

                n1=int(input("ingrese un numero: "))
                n2=int(input("ingrese un numero: "))
                cal = CalEstandar(n1,n2)
                cal.resta()
                input("Presione una tecla para continuar....")
                


            elif opc1 == "3":
                print("Calculadora Multiplicacion")
                print(" ")

                n1=int(input("ingrese un numero: "))
                n2=int(input("ingrese un numero: "))
                cal = CalEstandar(n1,n2)
                print("la multiplicacion de los 2 numero es:","{}*{}={}".format(n1,n2,cal.multiplicacion()))
                input("Presione una tecla para continuar....")
                



            elif opc1 == "4": 
                print("Calculadora Division")
                print(" ") 

                n1=int(input("ingrese un numero: "))
                n2=int(input("ingrese un numero: "))
                cal = CalEstandar(n1,n2)
                cal.division()

                input("Presione una tecla para continuar....")
                
        


            elif opc1 == "5": 
                print("Calculadora Exponente")
                print(" ") 

                n1=int(input("ingrese un numero: "))
                n2=int(input("ingrese un numero: "))
                cal = CalEstandar(n1,n2)
                cal.exponente()
                input("Presione una tecla para continuar....")
                


            elif opc1 == "6": 
                print("Calculadora Valor Absoluto")
                print(" ")

                n1=int(input("ingrese un numero: "))
                n2=0
                cal =CalEstandar(n1,n2)
                print("El valor absoluto es: ",cal.valorAbsoluto())
                
                input("Presione una tecla para continuar....")
                



            elif opc1 == "7": 
                print("Calculadora Circunferencia")
                print(" ") 

                n1 = int(input("Ingrese el valor del radio del circulo: "))
                n2=0
                cal = calCientifica(n1,n2)
                print("Valor de la superficie del radio es : ", cal.circunferencia())
                input("Presione una tecla para continuar....")
                



            elif opc1 == "8": 
                print("Calculadora Area Circulo")
                print(" ")
                n1=int(input("Ingrese el area: "))
                n2=0
                cal= calCientifica(n1,n2)
                print("Valor del Area Circulo es:",cal.areaCirculo())
                input("Presionne una tecla para continuar....")
                



            elif opc1 == "9": 
                print("Calculadora Area Cuadrado")
                print(" ")
                n1= int(input("Ingrese el area: "))
                n2=0
                cal= calCientifica(n1,n2)

                print("Valor del Area Cuadrado es:",cal.areaCuadrado())
                input("Presionne una tecla para continuar....")
                

                 


        
    # elif opc =="2":
    #     opc2 =""
    #     while opc1 !="11":
    #         print("Operación Numeros")
    #         men2=Menu("Menu secundario",["1)Presentar los números de 1 a n","2)Sumar los números de 1 a n","3)Múltiplo de cualquier numero","4)Presentar los divisores de un numero","5)Numero Primo","6)Factorial de cualquier numero","7)Fibonacci de una serie de n números","8)Perfecto","9)Primos gemelos","10)Números amigos","11)Salir"])
    #         opc2=men2.menu()
    #         os.system("cls") 
    #         if opc2 =="1":
    #             print("")

    #         elif opc1 == "2":
    #             print("Calculadora Resta")
    #             print(" ")  


    #         elif opc1 == "3":
    #             print("Calculadora Multiplicacion")
    #             print(" ")


    #         elif opc1 == "4": 
    #             print("Calculadora Division")
    #             print(" ") 


    #         elif opc1 == "5": 
    #             print("Calculadora Exponente")
    #             print(" ") 


    #         elif opc1 == "6": 
    #             print("Calculadora Valor Absoluto")
    #             print(" ") 


    #         elif opc1 == "7": 
    #             print("Calculadora Circunferencia")
    #             print(" ") 


    #         elif opc1 == "8": 
    #             print("Calculadora Area Circulo")
    #             print(" ")


    #         elif opc1 == "9": 
    #             print("Calculadora Area Cuadrado")
    #             print(" ")   


    # elif opc=="3":
    #     print("Tratamiento de Listas")
    #     men3=Menu("Menu secundario",["1)Recorrer y presentar los datos de una lista","2)Buscar un valor en una lista","3)Retornar una lista con los factoriales","4)Retornar una lista de números primos","5)Recorrer una lista de diccionario con notas de alumnos","6)Insertar un dato en una Lista dada lo Posición","7)Eliminar todas las ocurrencias en una Lista","8)Retornar cualquier valor de una lista eliminándolo ","9)Copiar cada elemento de una tupla en una lista","10)Dar el vuelto a varios clientes","11)Salir"])
    #     opc3=men3.menu()



    # elif opc=="4":
    #     print("Operaciones de  Cadenas")
    #     men4=Menu("Menu secundario",["1)Recorrer y presentar los datos de una cadena","2)Buscar un carácter en una cadena","3)Retornar una lista con la posiciones dado un carácter de la cadena","4)Retornar una lista con todas las palabras de una cadena","5)Retornar una cadena a partir de una lista","6)Insertar un dato en una cadena dada lo Posición","7)Eliminar todas las ocurrencias en una cadena","8)Retornar cualquier valor de una cadena eliminándolo ","9)Concatenar cadenas","10)Salir"])
    #     opc4=men4.menu()

    # elif opc=="5":
    #     print("Fuera del sistema")


    # else:
    #     print("Opcion no valida")
    #     print("","")
