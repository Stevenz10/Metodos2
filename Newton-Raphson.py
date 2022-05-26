import numpy as np
import sympy as smp
import scipy as sp
from scipy.misc import derivative



x = smp.symbols('x', real='True')

f = x**3-2*x-5
derivada = smp.diff(f,x)

def calcular(ecuacion,valor):
      return ecuacion.subs(x,valor).evalf()

# Newton-Raphson Algorithm
max_iter = 20  # Max iterations
tol = 1  # Tolerance
i = 0  # Iteration counter
x0 = 1  # Initial guess
xi_1 = x0

print('Iteration ' + str(i) + ': x = ' + str(x0) + ', f(x) = ' + str(calcular(f,x0)))
# Iterating until either the tolerance or max iterations is met
while abs(calcular(f,xi_1)) > tol or i > max_iter:
    i = i + 1
    xi = xi_1-calcular(f,xi_1)/calcular(derivada,xi_1)  # Newton-Raphson equation
    print('Iteration ' + str(i) + ': x = ' + str(xi) + ', f(x) = ' +    str(calcular(f,xi)))
    xi_1 = xi