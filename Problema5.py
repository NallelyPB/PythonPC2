'''Escribe un programa que encuentre la suma de todos los números primos menores que 100.'''


def Primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1): 
        if n % i == 0:
            return False
    return True


def Suma():
    suma = 0
    for num in range(2, 100):  # Desde 2 hasta 99
        if Primo(num):
            suma += num
    return suma

respuesta = Suma()
print(f'La suma de los numeros primos menores que 100 es: ', respuesta)