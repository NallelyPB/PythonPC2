'''Escribe un programa que encuentre todos los números perfectos menores que 1000. Un número
 perfecto es un número entero positivo que es igual a la suma de sus divisores propios positivos
 (excluyendo el propio número)'''

def Perfecto(num):
    suma=0
    for i in range (1,num):
        if num%i==0:
            suma +=i
    return suma==num

def Numeros_Perfectos(limite):
    num_perfectos=[]
    for i in range(1,limite):
        if Perfecto(i):
            num_perfectos.append(i)
    return num_perfectos

respuesta = Numeros_Perfectos(1000)

print("Números perfectos menores que 1000: ", respuesta)
        