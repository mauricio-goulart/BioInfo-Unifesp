"""
Created on Mon Aug 26 23:02:10 2024

Escreva um programa que receba uma string e retorne apenas as palavras
que possuem mais de três caracteres.

@author: mauricio
"""

############################################################

s1 = "Ola tudo bem"

lista = s1.split()

for p in lista:
    if len(p) > 3:
        print(p)

############################################################



