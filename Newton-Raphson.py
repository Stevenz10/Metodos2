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




opcion = 'S'

while opcion == 'S':
      try:
            x = Symbol('x')
            print("Ejemplo: x**3-2*x-5")
            ecuacion = parse_expr(input("Introduzca la ecuacion:\n"))
            graficar(ecuacion)
            x0 = int(input("Introduzca el punto inicial:\n"))  # Valor del punto inicial
            derivada = ecuacion.diff(x)
<<<<<<< HEAD
            # Newton-Raphson Algorithm
            max_iter = 30  # Max iterations
            tol = 1  # Tolerance    
            i = 0  # Iteration counter
=======
            # Inicio del Algoritmo Newton Raphson
            max_iter = 30  # Iteracion maxima
            tol = 1  # Minimo de error aceptado
            i = 0  # Contador de la iteracion
>>>>>>> 5e798acc32fb6dc7a5d2b7d7b90742f322628fa7
            xi_1 = x0

            valores = []

            while True:
                  xi = xi_1-calcular(ecuacion,xi_1)/calcular(derivada,xi_1)  # Ecuacion de Newton-Raphson 
                  valores.append([xi,calcular(ecuacion,xi)])
                  xi_1 = xi
                  if i>=1:
                        if abs(((valores[i][0]-valores[i-1][0])/valores[i][0])*100) < tol or i > max_iter:
                              break
                  i = i + 1
            for i,valor in enumerate(valores):
                  if i<1:
                        print('Iteration ' + str(i) + ': x = ' + str(valor[0]))
                  else:
                        print('Iteration ' + str(i) + ': x = ' + str(valor[0]) + ', error = ' +  str(abs(((valores[i][0]-valores[i-1][0])/valores[i][0])*100))+"%")
                  if i>30:
                        print('Hemos llegado a la iteracion maxima tolerada ' + str(i))
            opcion = input("Desea continuar S/N:  ").upper()
      except (SyntaxError,ValueError,TypeError):
            print("\n********************\nHa introducido un valor incorrecto\n********************\n")
      except :
            print("\n********************\nHa ocurrido un error inesperado\n********************\n")

print("\n********************\nCerrando programa\n********************\n")