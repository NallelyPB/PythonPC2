''' Al enviar mensajes de texto o twittear, no es raro acortar las palabras para ahorrar tiempo o espacio,
 por ejemplo, omitiendo las vocales.
 Implemente un programa que solicite al usuario una cadena de texto y luego retorne ese mismo
 texto pero con todas las vocales (A, E, I, O y U) omitidas, ya sea que se ingresen en mayúsculas o
 minúsculas.'''


def OmitirV(texto):
    vocales = "aeiouAEIOU"  
    nuevo_texto = ""   

    for caracter in texto:
        if caracter not in vocales: 
            nuevo_texto += caracter  

    return nuevo_texto

entrada = input("Ingrese una cadena de texto: ")
resultado = OmitirV(entrada)

print("Texto sin vocales:", resultado)
