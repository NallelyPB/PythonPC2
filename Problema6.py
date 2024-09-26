''' Escriba un programa en Python para obtener la serie de Fibonacci entre 0 y 50.'''

def Fibonacci(limite):
    fibo=[0,1]
    for _ in range(2,limite+1):
        sig_fibo=fibo[-1]+fibo[-2]
        if sig_fibo>limite:
            break
        fibo.append(sig_fibo)
    return fibo

respuesta= Fibonacci(50)
print(respuesta)
