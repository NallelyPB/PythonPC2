'''Escribe una función de Python para calcular el factorial de un número (un entero no negativo). La
 función acepta el número como argumento'''

def Factorial(num):
        if num < 0:
            print('Ingrese un numero entero no negativo')
            return
        elif num == 0 or num == 1:
            return 
        else:
            resultado = 1
            for i in range(2, num + 1):
                resultado *= i  
            return resultado
num = int(input('Ingrese un numero: '))
resultado = Factorial(num)
if resultado is not None:
    print(f"El factorial de {num} es: ", resultado)
