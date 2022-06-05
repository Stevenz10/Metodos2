import numpy as np
import matplotlib.pyplot as plt
from sympy import sympify, Symbol
from sympy.parsing.sympy_parser import parse_expr

def calcular(ecuacion,valor):
      x = Symbol('x')
      return ecuacion.subs(x,valor).evalf()
  
def graficar(ecuacion):
      valoresX = np.linspace(-5,5)
      valoresY = []
      for valor in valoresX:
            valoresY.append(calcular(ecuacion,valor))
      ax = plt.gca()
      ax.spines['top'].set_color('none')
      ax.spines['bottom'].set_position('zero')
      ax.spines['left'].set_position('zero')
      ax.spines['right'].set_color('none')      
      plt.title("Gráfica de " + str(ecuacion))
      plt.ylim(-10,10)
      plt.plot(valoresX,valoresY)
      plt.show()
      return None

# Implementing Regula Falsi Method
def Regula_Falsi(Xa,Xb,e):
    step = 1
    print('\n\n*** IMPLEMENTACIÓN DEL MÉTODO DE REGULA-FALSI ***')
    condition = True
    while condition:
        Xr = Xa- (Xb-Xa) * calcular(Xa)/( calcular(Xb) - calcular(Xa) )
        print('Iteración%d, Xr = %0.6f y f(Xr) = %0.6f' % (step, Xr, calcular(Xr)))

        if calcular(Xa) * calcular(Xr) < 0:
            Xb = Xr
        else:
            Xa = Xr

        step = step + 1
        condition = abs(calcular(Xr)) > e

    print('\nLa raíz requerida es: %0.8f' % Xr)


# Sección de Entrada
x = Symbol('x')
print("Ejemplo: -0.5*x**2+2.5*x+4.5")
ecuacion = parse_expr(input("Introduzca la ecuacion:\n"))
graficar(ecuacion)
Xa = input('Introduzca el primer número: ')
Xb = input('Introduzca el segundo número: ')
e = input('Introduzca el minímo error tolerable: ')

#Convertir las entradas en float
Xa = float(Xa)
Xb = float(Xb)
e = float(e)

#Revisando que los valores cumplan la teoria de Regula Falsi
if calcular(Xa) * calcular(Xb) > 0.0:
    print('Los valores ingresados no cumplen con las reglas de Regula Falsi.')
    print('Porfavor, vuelva a intentarlo de nuevo.')
else:
    Regula_Falsi(Xa,Xb,e)