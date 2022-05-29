from msilib.schema import _Validation_records
import numpy as np
import sympy as smp
import scipy as sp
from scipy.misc import derivative
import matplotlib.pyplot as plt


x = smp.symbols('x', real='True')

ecuacion = x**3-2*x-5
derivada = smp.diff(ecuacion,x)

def calcular(ecuacion,valor):
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
      plt.plot(valoresX,valoresY)
      plt.show()
      return None
# Newton-Raphson Algorithm
max_iter = 20  # Max iterations
tol = 1  # Tolerance
i = 0  # Iteration counter
x0 = 1  # Initial guess
xi_1 = x0

valores = []


print('Iteration ' + str(i) + ': x = ' + str(x0) + ', f(x) = ' + str(calcular(ecuacion,x0)))
# Iterating until either the tolerance or max iterations is met
while abs(calcular(ecuacion,xi_1)) > tol or i > max_iter:
    i = i + 1
    xi = xi_1-calcular(ecuacion,xi_1)/calcular(derivada,xi_1)  # Newton-Raphson equation
    valores.append([xi,calcular(ecuacion,xi)])
    xi_1 = xi

for i,valor in enumerate(valores):
      print('Iteration ' + str(i) + ': x = ' + str(valor[0]) + ', f(x) = ' +    str(valor[1]))

graficar(ecuacion)