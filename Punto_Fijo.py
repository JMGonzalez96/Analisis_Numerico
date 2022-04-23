# Antes de comenzar importamos algunas librerías que vamos a utilizar más adelante.

import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as opt

# Punto Fijo
# En este caso, vamos a utilizar una consigna que se encuentra en el libro Análisis Númerico de Richard Burden, Douglas Faires y Anette Burden, 10ma edición.

def fx (x):
    return x**4 - 3 * x**2 - 3

def gx (x):
    return  (3 * x**2 + 3) ** 0.25

# Genero una lista vacía para ir guardando las aproximaciones que se generar y luego poder imprimirlas.
lista=[]

def puntofijo(p0,N,TOL):
  i = 0
  while (i <= N):
      p = gx (p0)
      lista.append(p)
      if abs(p - p0) < TOL:
          print("La estimación es",p0,", se encontró en la iteración número",i,"con una tolerancia de",TOL)
          return p0
          break
      p0 = p
      i += 1
  else:
      print("No se pudo encontrar una aproximación")
      return False

# Definimos p0 que en este caso es 1 porque ya estaba preestablecido en la consigna del ejercicio.
# TOL es el error máximo aceptado que en este caso nos solicitan que sea de 0.01.
# N es la cantidad de iteraciones.
p = puntofijo(1,100,0.0001)

# Ponemos la condición de que se haga el gráfico y la tabla solo si el algoritmo funcionó
if p != False:


# Imprimimos los valores de p que se fueron obteniendo con las iteraciones
  print("n° | Aproximación")
  for n in range(len(lista)-1):
      print (n+1,"|",lista[n])

# Ahora utilizamos la función linspace de numpy que nos crea un vector con valores equidistantes, los cuales utilizamos para calcular la imagen de las funciones
  xi = np.linspace(1,2,20)
  fi = fx(xi)
  gi = gx(xi)
  yi = xi

# Por útlimo realizamos el gráfico de la función, un gráfico de la función g y una línea vertical en donde se grafica el valor de la aproximación.
  plt.plot(xi,fi, label='f(x)')
  plt.plot(xi,gi, label='g(x)')
  plt.plot(xi,yi, label='y=x')
  plt.axvline(p, color='r', label='p')
  plt.axhline(0, color='k')
  plt.title('Punto Fijo')
  plt.legend()
  plt.show()
