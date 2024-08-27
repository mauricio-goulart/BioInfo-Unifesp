"""
Created on Mon Aug 26 17:39:39 2024

Escreva uma rotina que recebe uma lista de números e retorna
outra lista contendo somente os números ímpares. Utilizar list
comprehension.

@author: mauricio
"""

############################################################

lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]

numeros_impares = [numero for numero in lista_numeros if numero % 2 != 0]

print("Números ímpares na lista:", numeros_impares)

############################################################


