''' Escribe un programa en Python para encontrar los números que son divisibles por 7 y múltiplos de 5,
 en el rango de 1500 y 2700 (ambos incluidos).''' 

lista =[]
for numero in range(1500,2700):
    if numero%7 == 0 and numero % 5==0:
        lista.append(numero)
    
print(lista)


