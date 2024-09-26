'''Por medio de un bucle While genere un código que permita el ingreso de números por teclado. El
 ingreso de los números debe ser permitido hasta que el usuario decida ya no ingresar nuevos
 números.
 Con dichos números, su programa debe evaluar cada uno de estos números e indicar la cantidad de
 números pares e impares.'''

lista =[]
while True:
    op = input('¿Desea ingresar un numero?').upper()
    if op== 'NO':
        break
    if op== 'SI':
        num = int(input('Ingrese el numero: '))
        lista.append(num)
    else:
        print('Respuesta inválida')

pares=0
impares=0
for numero in lista:
    if numero%2==0:
        pares+=1
    else:
        impares+=1

print('Numeros ingresados: ', lista)
print('Cantidad de numeros pares: ', pares)
print('Cantidad de numeros impares: ', impares)