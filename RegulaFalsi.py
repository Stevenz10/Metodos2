from wsgiref.validate import validator
import numpy as np
import matplotlib.pyplot as plt
from sympy import sympify, Symbol
from sympy.parsing.sympy_parser import parse_expr

def calcular(ecuacion,valor):
      x = Symbol('x')
      return ecuacion.subs(x,valor).evalf()
  
def graficar(ecuacion):
      valoresX = np.linspace(-10,10)
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

# Implementando Regula Falsi Method
def Regula_Falsi(Xa,Xb,e,ecuacion):
    step = 0
    print('\n\n*** IMPLEMENTACIÓN DEL MÉTODO DE REGULA-FALSI ***')
    condition = True
    while condition:
        Xr = Xa- (Xb-Xa) * calcular(ecuacion,Xa)/( calcular(ecuacion,Xb) - calcular(ecuacion,Xa) )
        valores.append([Xr,Xa,Xb])
        if step>=1:
            print('Iteración%d, Xr = %0.6f y error = %0.6f' % (step, Xr, abs(((valores[step][0]-valores[step-1][0])/valores[step][0])*100)) + "%")
        else:
            print('Iteración%d, Xr = %0.6f' % (step, Xr))
        if calcular(ecuacion,Xa) * calcular(ecuacion,Xr) < 0:
            Xb = Xr
        else:
            Xa = Xr
        if step>=1:
            condition = abs(((valores[step][0]-valores[step-1][0])/valores[step][0])*100) > e
        step = step + 1

    print('\nLa raíz requerida es: %0.8f' % Xr)

# Sección de Entrada
opcion = 'S'

while opcion == 'S':
    try:
        x = Symbol('x')
        print("Ejemplo: -0.5*x**2+2.5*x+4.5")
        ecuacion = parse_expr(input("Introduzca la ecuacion:\n"))
        graficar(ecuacion)
        Xa = float(input('Introduzca el primer número: '))
        Xb = float(input('Introduzca el segundo número: '))
        e = float(input('Introduzca el minímo error tolerable: '))

        valores = []

        #Revisando que los valores cumplan la teoria de Regula Falsi
        if calcular(ecuacion,Xa) * calcular(ecuacion,Xb) > 0.0:
            print('Los valores ingresados no cumplen con las reglas de Regula Falsi.')
            print('Porfavor, vuelva a intentarlo de nuevo.')
        else:
            Regula_Falsi(Xa,Xb,e,ecuacion)
        opcion = input("Desea continuar S/N:  ").upper()
    except (SyntaxError,ValueError,TypeError):
        print("\n********************\nHa introducido un valor incorrecto\n********************\n")
    except :
        print("\n********************\nHa ocurrido un error inesperado\n********************\n")


print("\n********************\nCerrando programa\n********************\n")
