'''En los Estados Unidos, las fechas suelen tener el siguiente formato: mes-día-año (MM/DD/AAAA). Las
 fechas en ese formato no se pueden ordenar fácilmente porque el año de la fecha es el último en
 lugar del primero. Intente ordenar, por ejemplo, 2/2/1800, 3/3/1900 y 1/1/2000 cronológicamente
 en cualquier programa (por ejemplo, una hoja de cálculo). Las fechas en ese formato también son
 ambiguas. ¡Una fecha como el 8 de septiembre de 1636, podría interpretarse como el 9 de agosto de
 1636!
 Implementar un programa que pida al usuario una fecha, en orden mes-día-año, con formato como
 8/9/1636 o Septiembre 8, 1636, donde el mes en este último podría ser cualquiera de los valores en
 la lista abajo:
 [
 ]
 "Enero",
 "Febrero",
 "Marzo",
 "Abril",
 "Mayo",
 "Junio",
 "Julio",
 "Agosto",
 "Septiembre",
 "Octubre",
 "Noviembre",
 "Diciembre"'''
def es_numero(s):
    for char in s:
        if char < '0' or char > '9':
            return False
    return True

def convertir_fecha(fecha):
    meses = {
        "Enero": 1,
        "Febrero": 2,
        "Marzo": 3,
        "Abril": 4,
        "Mayo": 5,
        "Junio": 6,
        "Julio": 7,
        "Agosto": 8,
        "Septiembre": 9,
        "Octubre": 10,
        "Noviembre": 11,
        "Diciembre": 12
    }

    if '/' in fecha:
        partes = fecha.split('/')
        if len(partes) == 3:
            mes = partes[0]
            dia = partes[1]
            anio = partes[2]
            if es_numero(mes) and es_numero(dia) and es_numero(anio):
                mes = int(mes)
                dia = int(dia)
                anio = int(anio)
                if 1 <= mes <= 12 and 1 <= dia <= 31:  
                    return f"{anio}-{mes:02}-{dia:02}"

    if ',' in fecha:
        partes = fecha.split(' ', 1)
        if len(partes) == 2:
            mes_str = partes[0]
            dia_anio = partes[1].split(',')
            if len(dia_anio) == 2:
                dia = dia_anio[0].strip()
                anio = dia_anio[1].strip()
                if es_numero(dia) and es_numero(anio) and mes_str in meses:
                    dia = int(dia)
                    anio = int(anio)
                    mes = meses[mes_str]
                    if 1 <= dia <= 31:  
                        return f"{anio}-{mes:02}-{dia:02}"

    return "Formato de fecha no válido."

fecha_usuario = input("Ingrese una fecha (MM/DD/AAAA o 'Mes día, año'): ")
resultado = convertir_fecha(fecha_usuario)

print("Fecha en formato AAAA-MM-DD:", resultado)

