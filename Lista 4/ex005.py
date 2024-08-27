"""
Created on Mon Aug 26 22:30:23 2024

Escreva uma função em Python que receba uma string como entrada e
verifique se ela é um palíndromo.

@author: mauricio
"""

############################################################

p1 = input("Digite uma palavra: ")
lista = []

for char in range(len(p1) - 1, -1, -1):
    lista.append(p1[char])
    
p2 = "".join(lista)

if p1 == p2:
    print("Palindromo")   
    
else:
    print("Nao e palindromo")

############################################################

