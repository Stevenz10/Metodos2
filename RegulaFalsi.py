import matplotlib.pyplot as plt
from numpy import linspace

# Definiendo función
def f(x):
    return -0.5*x**2+2.5*x+4.5

# Implementing Regula Falsi Method
def Regula_Falsi(Xa,Xb,e):
    step = 1
    print('\n\n*** IMPLEMENTACIÓN DEL MÉTODO DE REGULA-FALSI ***')
    condition = True
    while condition:
        Xr = Xa- (Xb-Xa) * f(Xa)/( f(Xb) - f(Xa) )
        print('Iteración%d, Xr = %0.6f y f(Xr) = %0.6f' % (step, Xr, f(Xr)))

        if f(Xa) * f(Xr) < 0:
            Xb = Xr
        else:
            Xa = Xr

        step = step + 1
        condition = abs(f(Xr)) > e

    print('\nLa raíz requerida es: %0.8f' % Xr)


# Sección de Entrada
Xa = input('Introduzca el primer número: ')
Xb = input('Introduzca el segundo número: ')
e = input('Introduzca el minímo error tolerable: ')

#Convertir las entradas en float
Xa = float(Xa)
Xb = float(Xb)
e = float(e)

#Revisando que los valores cumplan la teoria de Regula Falsi
if f(Xa) * f(Xb) > 0.0:
    print('Los valores ingresados no cumplen con las reglas de Regula Falsi.')
    print('Porfavor, vuelva a intentarlo de nuevo.')
else:
    Regula_Falsi(Xa,Xb,e)

#Gráfica de Regula Falsi
x = linspace(-3,8,100)
ax = plt.gca()
ax.spines['top'].set_color('none')
ax.spines['bottom'].set_position('zero')
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')      
plt.plot(x,f(x))
plt.title("Gráfica de -0.5*x**2+2.5*x+4.5")
plt.grid(True)
plt.show()