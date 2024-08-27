"""
Created on Mon Aug 26 22:42:38 2024

Escreva uma função em Python que receba uma string como entrada e retorne
a string com cada palavra em ordem inversa.

@author: mauricio
"""

############################################################

s1 = "Ola bom dia"
lista = s1.split()
lista2 = []

for p in lista:
    lista2.append(p[::-1])
    
s2 = " ".join(lista2)
    
############################################################

