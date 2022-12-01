def biseccion(f, a, b, tol, iteracion=1):
    if f(a)*f(b) >= 0:
        print("En el intervalo especificado no existe raíz para la función.")
    x = (a + b)/2

    if -tol < f(x) < tol:
        return x, iteracion

    elif f(a)*f(x) >= 0:
        return biseccion(f, x, b, tol, iteracion+1)
     
    elif f(b)*f(x) >= 0:
        return biseccion(f, a, x, tol, iteracion+1)


 
f = lambda x: x**3 + x + 16
x, iteraciones = biseccion(f, -4, 0, 1e-3)
print("Raíz estimada por método de la bisección:", x)
print("N° de iteraciones:", iteraciones)

def secante(f, a, b, tol, iteracion=1):

    if f(a)*f(b) >= 0 and iteracion==1:

        print("En el intervalo especificado no existe raíz para la función.")
        
    x = b - f(b)*((b - a)/(f(b) - f(a)))

    if -tol < f(x) < tol:
        return x, iteracion

    return secante(f, b, x, tol, iteracion+1)
   
f = lambda x: x**3 + x + 16
x, iteraciones = secante(f, -4, 0, 1e-3)
print("Raíz estimada por método de la secante:", x)
print("N° de iteraciones:", iteraciones)


def newton_raphson(f, x0, tol, iteracion=1):

    dfx0 = (f(x0 + tol/2) - f(x0 - tol/2)) / tol

    x = x0 - f(x0)/dfx0

    if -tol < f(x) < tol:
        return x, iteracion
    
    return newton_raphson(f, x, tol, iteracion+1)


  
f = lambda x: x**3 + x + 16
x, iteraciones = newton_raphson(f, 0, 1e-3)
print("Raíz estimada por método de Newton-Raphson:", x)
print("N° de iteraciones:", iteraciones)
