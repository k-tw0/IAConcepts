"""

Álgebra lineal:

El álgebra lineal es una rama de las matemáticas que se enfoca en el estudio
de los espacios vectoriales y sus propiedades. 
En términos más simples, el álgebra lineal se utiliza para resolver sistemas
de ecuaciones lineales y para describir la geometría de objetos en el espacio.

Un ejemplo de álgebra lineal en Python sería utilizar la librería NumPy
para realizar operaciones matemáticas con vectores y matrices. 
Por ejemplo, podríamos crear un vector en Python utilizando la siguiente sintaxis:

"""
#ejemplo de una operación de álgebra lineal que se puede realizar con vectores de NumPy:

#Por lo tanto, el producto punto se calcula como:
#1.0 * 4.0 + 2.0 * 5.0 + 3.0 * 6.0 = 4.0 + 10.0 + 18.0 = 32.0

import numpy as np

# Crear dos vectores con NumPy
vector_a = np.array([1.0, 2.0, 3.0])
vector_b = np.array([4.0, 5.0, 6.0])

# Calcular el producto punto (dot product) entre los dos vectores
producto_punto = np.dot(vector_a, vector_b)

print("El producto punto de los vectores a y b es:", producto_punto)

#Luego, podríamos realizar diversas operaciones matemáticas con este vector,
#como la suma de vectores o la multiplicación por una matriz.


"""

Cálculo:

El cálculo es otra rama importante de las matemáticas, que se utiliza para estudiar
la variación y el cambio de las funciones matemáticas. En particular, el cálculo
se enfoca en el cálculo de derivadas e integrales, y en la aplicación de estas 
técnicas para resolver problemas en diversas áreas de la ciencia y la ingeniería.

En Python, podemos utilizar la librería SciPy para realizar cálculo numérico.
Por ejemplo, podríamos utilizar la función "derivative" de SciPy
para calcular la derivada de una función en un punto dado:


CODIGO ANTIGUO:

from scipy.misc import derivative

# Definir una función en Python
def f(x):
    return x**2 + 3*x + 1

# Calcular la derivada de f en x=2
derivada = derivative(f, 2)

print(derivada)

"""

"""

El aviso de deprecación que estás recibiendo se debe a que la función scipy.misc.derivative
que estás utilizando ha sido marcada como obsoleta a partir de la versión 1.10.0 de Scipy.
Esto significa que la función todavía funciona en la versión actual de Scipy,
 pero es posible que no esté disponible en futuras versiones y que deba ser reemplazada por una alternativa.

En el caso de scipy.misc.derivative, la alternativa recomendada en el mensaje
de advertencia es utilizar una de las siguientes bibliotecas:

findiff: una biblioteca que proporciona herramientas para la diferenciación numérica. 
Puedes encontrar más información sobre findiff en su repositorio de GitHub: https://github.com/maroba/findiff

numdifftools: una biblioteca que proporciona herramientas para la diferenciación numérica,
la integración y la optimización. Puedes encontrar más información sobre numdifftools
en su repositorio de GitHub: https://github.com/pbrod/numdifftools

"""

from numdifftools import Derivative

# Definir una función en Python
def f(x):
    return x**2 + 3*x + 1  # Esta ecuación puede cambiar

# Calcular la derivada de f en x=2
derivada_en_x_2 = Derivative(f)(2)  # Derivate viene de numdifftools, librería que llama a la función derivate para calcular derivadas de una función.

print(derivada_en_x_2)

# En este ejemplo, la función "f" representa una función matemática, y
# la función "derivative" de SciPy se utiliza para calcular su derivada en el punto x=2.


"""

Probabilidad:

La probabilidad es una rama de las matemáticas que se enfoca en el estudio de eventos aleatorios
y la cuantificación de la incertidumbre. En particular, la probabilidad se utiliza para describir
y predecir la ocurrencia de eventos inciertos en diversos campos, como la física, la economía y la biología.

En Python, podemos utilizar la librería NumPy para realizar operaciones de probabilidad.
Por ejemplo, podríamos utilizar la función "random" de NumPy para simular el lanzamiento de un dado:

"""

import numpy as np

# Simular el lanzamiento de un dado con NumPy
dado = np.random.randint(1, 7, size=2)

print(dado)




