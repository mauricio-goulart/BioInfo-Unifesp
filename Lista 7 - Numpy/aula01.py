"""
Created on Tue Aug 27 20:36:13 2024

Aprendendo usar Numpy

@author: mauricio
"""

#Imports:    
import numpy as np

############################################################

#Iniciando uma matriz e multiplicando por 3
matrix = np.array([[1,2,3], [4,5,6], [7,8,9]])

print(3 * matrix)

#Mostrar numero indice do array
print("\n", matrix[0:2, 0:2]) # Mostra a 1,2 linha e 1,2 coluna

############################################################

#Extraindo informações do ndarray
print(f"\nDimensões = [{matrix.ndim}]")
print(f"Formato = [{matrix.shape}]")
print(f"Quantidade de elementos = [{matrix.size}]")
print(f"Tipo dos elementos = [{matrix.dtype}]")

############################################################

#Formas de iniciar arrays
m = np.array([[1,2,3], [2,4,6]]) # Cria array a partir de um conjunto de listas
print("\n", m)

m = np.arange(0,10,1) # Cria array similiar ao range
print("\n", m)

m = np.zeros((3,3)) # Cria array com zeros
print("\n", m)

m = np.ones((2,2)) # Cria array com um
print("\n", m)

m = np.zeros_like(m) # Cria um array com zeros no mesmo formato do array passado como ref
print("\n", m)

m = np.ones_like(m) # Cria um array com um no mesmo formato do array passado como ref
print("\n", m)

m = np.linspace(0,3,4) # Cria um array que começa no a e termina no b com c passos
print("\n", m)

m = np.random.randint(0, 99, (4,4)) # Cria um array com numeros aleatorios do a até b no formato c
print("\n", m)

############################################################

#Alterar o tipo de variavel do array
m = np.ones((3,3), dtype=np.int8) * 5
print("\n", m)

m = m.astype(np.int64) # astype muda o tipo da variavel da array 

############################################################

#Operações com matrizes - Elemento por elemento
a = np.array([[3, 6, 9], [10, 5, 4]])
b = np. array([[4, 2, 1], [5, 1, 9]])
c = a + b

print("\n", c) # Soma e subtração e multiplição(elemento por elemento) e divisão de arrays

#Operações com escalar
a = np.array([[3,6,8], [3,3,3]])
c = 3 + a

print("\n", c) # Soma e subtração etc por escalar

#Operações usada na algebra linear
a = np.array([[2,4], [8,6]])
b = np.array([[3,6], [5,10]])
c = np.dot(a,b)

print("\n", c) # Multiplicação usada de array algebra linear

#Matriz Inversa
a = np.array([[4,6], [8,2]])
b = np.linalg.inv(a)

print("\n", b) # Matriz Inversa

#Determinante
a = np.array([[4,6], [8,2]])
b = np.linalg.det(a)

print("\n", b) # Determinante da matriz

#Matriz transposta
a = np.array([[4,6,2], [8,2,4]])
b = a.T

print("\n", b) # Matriz transposta virada a 90º

############################################################

#Extraindo mais informações - Minimo Matriz e max -> .max
a = np.array([[2,5,3] , [3,7,6]])

print("\n", a.min()) # valor minimo da  matriz
print("\n", a.min(0)) # valor minimo da coluna da matriz
print("\n", a.min(1)) # valor minimo da linha da matriz

#Somando todos numeros da matriz
a = np.array([[2,5,3] , [3,7,6]])

print("\n", a.sum()) # soma de todos elementos matriz
print("\n", a.sum(0)) # soma coluna matriz
print("\n", a.sum(1)) # soma linha matriz

#Soma acumulativa
a = np.array([[2,5,3] , [3,7,6]])

print("\n", a.cumsum()) # soma acumulativa matriz

#Media matriz
a = np.array([[2,5,3] , [3,7,6]])

print("\n", a.mean()) # media de todos elementos matriz
print("\n", a.mean(0)) # media coluna matriz
print("\n", a.mean(1)) # media linha matriz

#Desvio padrão matriz
a = np.array([[2,5,3] , [3,7,6]])

print("\n", a.std()) # desvio padrão de todos elementos matriz
print("\n", a.std(0)) # desvio padrão coluna matriz
print("\n", a.std(1)) # desvio padrão linha matriz

############################################################






